from Booker.src.api.booking_api import BookingAPI
from Booker.src.data_models.booking_models import BookingData
from Booker.src.utils.validator import validate_data


class BookingScenarios(BookingAPI):
    def __init__(self, base_url, auth_session):
        super().__init__(base_url, auth_session)

        self._data_create_name = 'booking'

    def _get_item_from_array(self, item_id, arr):
        res_arr = list(filter(lambda i: i[self._id_name] == item_id, arr))
        assert len(res_arr) > 0, 'Элемент не найден'
        assert item_id == res_arr[0][self._id_name], f"Нет созданой записи"
        return res_arr[0][self._id_name]

    def create_booking(self, data):
        response, id = self.create_item(data)
        validate_data(response,
                      BookingData,
                      data,
                      self._data_create_name)
        self.delete_item(id)

    def update_booking(self, data, update_data):
        response_create, id = self.create_item(data)
        validate_data(response_create,
                      BookingData,
                      data,
                      self._data_create_name)
        response_update = self.update_item(id, update_data)
        validate_data(response_update, BookingData, update_data)
        self.delete_item(id)

    def partial_update_booking(self, data, partial_update_data):
        response_create, id = self.create_item(data)
        validate_data(response_create,
                      BookingData,
                      data,
                      self._data_create_name)
        response_update = self.partial_update_item(id, partial_update_data)
        validate_data(response_update, BookingData, data)
        self.delete_item(id)

    def get_booking(self, data):
        response_create, id = self.create_item(data)
        validate_data(response_create,
                      BookingData,
                      data,
                      self._data_create_name)
        response_get = self.get_item(id)
        validate_data(response_get, BookingData, data)
        self.delete_item(id)

    def get_booking_by_fullname(self, data):
        response_create, id = self.create_item(data)
        validate_data(response_create,
                      BookingData,
                      data,
                      self._data_create_name)
        filter_url = f"?firstname={data['firstname']}&lastname={data['lastname']}"
        response_get = self.get_items(filter_url)
        self._get_item_from_array(id, response_get)
        self.delete_item(id)

    def get_booking_by_firstname(self, data):
        response_create, id = self.create_item(data)
        validate_data(response_create,
                      BookingData,
                      data,
                      self._data_create_name)
        filter_url = f"?firstname={data['firstname']}"
        response = self.get_items(filter_url)
        self._get_item_from_array(id, response)
        self.delete_item(id)

    def get_booking_by_lastname(self, data):
        response_create, id = self.create_item(data)
        validate_data(response_create,
                      BookingData,
                      data,
                      self._data_create_name)
        filter_url = f"?lastname={data['lastname']}"
        response = self.get_items(filter_url)
        self._get_item_from_array(id, response)
        self.delete_item(id)

    def get_booking_by_bookingdates(self, data):
        response_create, id = self.create_item(data)
        validate_data(response_create,
                      BookingData,
                      data,
                      self._data_create_name)
        checkin = data['bookingdates']['checkin']
        checkout = data['bookingdates']['checkout']
        filter_url = f"?checkin={checkin}&checkout={checkout}"
        response = self.get_items(filter_url)
        self._get_item_from_array(id, response)
        self.delete_item(id)

    def get_booking_by_checkin_date(self, data):
        response_create, id = self.create_item(data)
        validate_data(response_create,
                      BookingData,
                      data,
                      self._data_create_name)
        checkin = data['bookingdates']['checkin']
        filter_url = f"?checkin={checkin}"
        response = self.get_items(filter_url)
        self._get_item_from_array(id, response)
        self.delete_item(id)

    def get_booking_by_checkout_date(self, data):
        response_create, id = self.create_item(data)
        validate_data(response_create,
                      BookingData,
                      data,
                      self._data_create_name)
        checkout = data['bookingdates']['checkout']
        filter_url = f"?checkout={checkout}"
        response = self.get_items(filter_url)
        self._get_item_from_array(id, response)
        self.delete_item(id)
