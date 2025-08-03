from requests import Response
import pytest
from Booker.src.utils.validator import validate_response
from Booker.src.data_models.booking_models import BookingData, BookingResponseCreate, BookingResponseGetItems


class BookingAPI:
    def __init__(self, base_url, auth_session):
        self.auth_session = auth_session
        self.base_url = base_url
        self.action_url = 'booking'
        self._id_name = "bookingid"

    def get_item(self, item_id):
        url = f"{self.base_url}/{self.action_url}/{item_id}"
        get = self.auth_session.get(url)
        return validate_response(get, model=BookingData)

    def get_items(self, filter_url=''):
        url = f"{self.base_url}/{self.action_url}{filter_url}"
        get = self.auth_session.get(url)
        return validate_response(get,
                                 model=BookingResponseGetItems,
                                 isList=True)

    def create_item(self, item_data):
        url = f"{self.base_url}/{self.action_url}"
        create: Response = self.auth_session.post(url, json=item_data)
        return validate_response(create,
                                 model=BookingResponseCreate,
                                 return_field=self._id_name)

    def update_item(self, item_id, item_data):
        url = f"{self.base_url}/{self.action_url}/{item_id}"
        update = self.auth_session.put(url, json=item_data)
        return validate_response(update, model=BookingData)

    def partial_update_item(self, item_id, item_update_data):
        url = f"{self.base_url}/{self.action_url}/{item_id}"
        update = self.auth_session.patch(url, json=item_update_data)
        return validate_response(update, model=BookingData)

    def delete_item(self, item_id):
        url = f"{self.base_url}/{self.action_url}/{item_id}"
        delete = self.auth_session.delete(url)
        get = self.auth_session.get(url)
        validate_response(delete, expected_status=201)
        validate_response(get, expected_status=404)

        # assert delete.status_code == 201, f"Ошибка удаления данных {url}"
        # assert get.status_code == 404, "Данные не удалились"
