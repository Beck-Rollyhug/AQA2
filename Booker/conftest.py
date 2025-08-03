from faker import Faker
import requests
import pytest

from constant import BASE_URL, HEADERS, AUTH_JSON

faker = Faker()


@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    response = requests.post(
        f"{BASE_URL}/auth", headers=HEADERS, json=AUTH_JSON)
    assert response.status_code == 200, f"auth error"
    token = response.json().get("token")
    assert token is not None, "no auth token"

    session.headers.update({"Cookie": f"token={token}"})
    return session


@pytest.fixture()
def booking_partial_update_data():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
    }


@pytest.fixture()
def booking_data():
    def _create_data_from(booking_partial_update_data: dict[str] | None = None):
        print('booking_partial_update_data', booking_partial_update_data)
        if (not booking_partial_update_data):
            return {
                "firstname": faker.first_name(),
                "lastname": faker.last_name(),
                "totalprice": faker.random_int(min=1000, max=9000, step=100),
                "depositpaid": True,
                "bookingdates": {
                    "checkin": "2017-12-30",
                    "checkout": "2019-01-01"
                },
                "additionalneeds": "Breakfast"
            }
        else:
            return {
                "firstname": booking_partial_update_data['firstname'],
                "lastname": booking_partial_update_data['lastname'],
                "totalprice": faker.random_int(min=1000, max=9000, step=100),
                "depositpaid": True,
                "bookingdates": {
                    "checkin": "2017-12-30",
                    "checkout": "2019-01-01"
                },
                "additionalneeds": "Breakfast"
            }

    return _create_data_from


@pytest.fixture()
def booking_update_data():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=1000, max=9000, step=100),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
