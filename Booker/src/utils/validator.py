import pytest
from pydantic import BaseModel, ValidationError
from requests import Response


def check_and_get_json(response: Response, expected_status: int = 200):
    if response.status_code != expected_status:
        pytest.fail(
            f"Expected status {expected_status}, got {response.status_code}: {response.text}")
    try:
        response_json = response.json()
        return response_json
    except Exception as e:
        pytest.fail(f"Ошибка парсинга JSON: {e}\nResponse: {response.text}")


def validate_schema(data, model: BaseModel, isList: bool | None = None):
    try:
        if isList:
            return [model(**item) for item in data]
        return model(**data)
    except ValidationError as e:
        pytest.fail(f"Pydantic валидация структуры не прошла:\n{e}")


def compare_with_expected(parsed_data: BaseModel, expected_data, data_model: BaseModel):
    parsed_expected: BaseModel = data_model(**expected_data)
    actual_data_dump = parsed_data.model_dump(exclude_unset=True)
    expected_data_dump = parsed_expected.model_dump(exclude_unset=True)

    if actual_data_dump != expected_data_dump:
        pytest.fail(
            f"Данные ответа не совпадают с ожидаемыми:\n"
            f"Expected: {expected_data_dump}\n"
            f"Actual:   {actual_data_dump}"
        )


def try_get_field(data, field_name):
    try:
        return getattr(data, field_name)
    except ValidationError as e:
        pytest.fail(f"Pydantic в данной модели нет поля {field_name}:\n{e}")


"""
Универсальный валидатор ответа API:
- Проверка status_code
- Валидация схемы ответа через Pydantic
- Получение конкретного поля из результата (опционально)

:return: json ответа, поле из результата (опционально)
"""


def validate_response(
    response: Response,
    expected_status: int = 200,
    model: BaseModel | None = None,
    isList: bool | None = None,
    return_field: str | None = None,
) -> BaseModel:
    response_json = check_and_get_json(response, expected_status)
    if not model:
        return response_json

    if (isList and len(response_json) == 0):
        pytest.fail(f"В ответе пустой массив")

    parsed_response = validate_schema(response_json, model, isList)
    if return_field and not isList:
        return response_json, try_get_field(parsed_response, return_field)
    return response_json


"""
Универсальный валидатор данных:
- Валидация схемы через Pydantic
- Сравнение с ожидаемыми данными (опционально)
- Сравнение вложенного объекта с ожидаемыми данными (опционально)
"""


def validate_data(
    data: dict,
    model: BaseModel,
    expected_data: dict,
    data_root_field: str | None = None,
) -> BaseModel:
    data_to_validate = data if not data_root_field else data[data_root_field]
    parsed_data: BaseModel = model(**data_to_validate)
    parsed_expected: BaseModel = model(**expected_data)
    actual_data_dump = parsed_data.model_dump(exclude_unset=True)
    expected_data_dump = parsed_expected.model_dump(exclude_unset=True)

    if actual_data_dump != expected_data_dump:
        pytest.fail(
            f"Данные ответа не совпадают с ожидаемыми:\n"
            f"Expected: {expected_data_dump}\n"
            f"Actual:   {actual_data_dump}"
        )
