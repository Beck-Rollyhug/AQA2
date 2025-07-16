import pytest

from Booker.constant import BASE_URL


class TestBookings:
    def __get_booking(self, auth_session, booking_id):
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, f"Новая запись не найдена"
        response_data = get_booking.json()
        booking_id = response_data.get("bookingid")
        assert booking_id is not None, "Запись не найдена"

        return response_data

    def __create_booking(self, auth_session, booking_data):
        create_booking = auth_session.post(
            f"{BASE_URL}/booking", json=booking_data)
        response_data = create_booking.json()
        booking_id = response_data.get("bookingid")

        assert booking_id is not None, "Ошибка создания тестовых данных"
        return booking_id

    def __delete_booking(self, auth_session, booking_id):
        delete_booking = auth_session.delete(
            f"{BASE_URL}/booking/{booking_id}")
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")

        assert delete_booking.status_code == 201, f"Ошибка очистки тестовых данных"
        assert get_booking.status_code == 404, f"Тестовые данные не удалились"

    def test_create_booking(self, auth_session, booking_data):
        create_booking = auth_session.post(
            f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, f"Ошибка создания записи"
        response_data = create_booking.json()
        booking_id = response_data.get("bookingid")
        assert booking_id is not None, "У новой записи нет ID"

        isNameMatch = response_data['booking']['firstname'] == booking_data['firstname']
        isPriceMatch = response_data['booking']['totalprice'] == booking_data['totalprice']
        assert isNameMatch, "Не установились нужные данные"
        assert isPriceMatch, "Не установились нужные данные"

        self.__delete_booking(auth_session, booking_id)

    def test_update_booking(
            self,
            auth_session,
            booking_data,
            booking_update_data):
        booking_id = self.__create_booking(auth_session, booking_data)

        update_booking = auth_session.put(
            f"{BASE_URL}/booking/{booking_id}", json=booking_update_data)
        assert update_booking.status_code == 200, f"Ошибка обновления записи"

        response_data = update_booking.json()
        isNameMatch = response_data['firstname'] == booking_update_data['firstname']
        isPriceMatch = response_data['totalprice'] == booking_update_data['totalprice']
        assert isNameMatch, "Не установилось новое имя"
        assert isPriceMatch, "Не установилось новая цена"

        self.__delete_booking(auth_session, booking_id)

    def test_partial_update_booking(
            self,
            auth_session,
            booking_data,
            booking_partial_update_data):
        booking_id = self.__create_booking(auth_session, booking_data)

        partial_update_booking = auth_session.patch(
            f"{BASE_URL}/booking/{booking_id}",
            json=booking_partial_update_data)
        assert partial_update_booking.status_code == 200, f"Ошибка обновления записи"

        response_data = partial_update_booking.json()
        isNameMatch = response_data['firstname'] == booking_partial_update_data['firstname']
        isLastNameMatch = response_data['lastname'] == booking_partial_update_data['lastname']
        assert isNameMatch, "Не установилось новое имя"
        assert isLastNameMatch, "Не установилось новая фамилия"

        self.__delete_booking(auth_session, booking_id)

    def test_get_booking(self, auth_session):
        get_booking = auth_session.get(f"{BASE_URL}/booking")
        assert get_booking.status_code == 200, f"Ошибка получения записей"

        response_data = get_booking.json()
        assert len(response_data) > 0, f"Пустой массив данных"

    def test_get_booking_by_fullname(self, auth_session, booking_data):
        # фильтрация запроса по полному имени

        booking_id = self.__create_booking(auth_session, booking_data)
        firstname = booking_data['firstname']
        lastname = booking_data['lastname']

        get_bookingIDs = auth_session.get(
            f"{BASE_URL}/booking/?firstname={firstname}&lastname={lastname}")
        assert get_bookingIDs.status_code == 200, f"Ошибка получения записей"

        response_data = get_bookingIDs.json()
        assert len(response_data) > 0, f"Пустой ответ"

        response_item_id = None
        for item in response_data:
            if (item['bookingid'] == booking_id):
                response_item_id = item['bookingid']

        assert booking_id == response_item_id, f"Нет созданой записи"

        self.__delete_booking(auth_session, booking_id)

    def test_get_booking_by_firstname(self, auth_session, booking_data):
        # фильтрация запроса по имени

        booking_id = self.__create_booking(auth_session, booking_data)
        firstname = booking_data['firstname']

        get_bookingIDs = auth_session.get(
            f"{BASE_URL}/booking/?firstname={firstname}")
        assert get_bookingIDs.status_code == 200, f"Ошибка получения записей"

        response_data = get_bookingIDs.json()
        assert len(response_data) > 0, f"Пустой ответ"

        response_item_id = None
        for item in response_data:
            if (item['bookingid'] == booking_id):
                response_item_id = item['bookingid']

        assert booking_id == response_item_id, f"Нет созданой записи"

        self.__delete_booking(auth_session, booking_id)

    def test_get_booking_by_lastname(self, auth_session, booking_data):
        # фильтрация запроса по полному имени

        booking_id = self.__create_booking(auth_session, booking_data)
        lastname = booking_data['lastname']

        get_bookingIDs = auth_session.get(
            f"{BASE_URL}/booking/?lastname={lastname}")
        assert get_bookingIDs.status_code == 200, f"Ошибка получения записей"

        response_data = get_bookingIDs.json()
        assert len(response_data) > 0, f"Пустой ответ"

        response_item_id = None
        for item in response_data:
            if (item['bookingid'] == booking_id):
                response_item_id = item['bookingid']

        assert booking_id == response_item_id, f"Нет созданой записи"

        self.__delete_booking(auth_session, booking_id)

    def test_get_booking_by_bookingdates(self, auth_session, booking_data):
        # фильтрация запроса по датам

        booking_id = self.__create_booking(auth_session, booking_data)
        checkin = booking_data['bookingdates']['checkin']
        checkout = booking_data['bookingdates']['checkout']

        get_bookingIDs = auth_session.get(
            f"{BASE_URL}/booking/?checkin={checkin}&checkout={checkout}")
        assert get_bookingIDs.status_code == 200, f"Ошибка получения записей"

        response_data = get_bookingIDs.json()
        assert len(response_data) > 0, f"Пустой ответ"

        response_item_id = None
        for item in response_data:
            if (item['bookingid'] == booking_id):
                response_item_id = item['bookingid']

        assert booking_id == response_item_id, f"Нет созданой записи"

        self.__delete_booking(auth_session, booking_id)

    def test_get_booking_by_checkin_date(self, auth_session, booking_data):
        # фильтрация запроса по датам

        booking_id = self.__create_booking(auth_session, booking_data)
        checkin = booking_data['bookingdates']['checkin']

        get_bookingIDs = auth_session.get(
            f"{BASE_URL}/booking/?checkin={checkin}")
        assert get_bookingIDs.status_code == 200, f"Ошибка получения записей"

        response_data = get_bookingIDs.json()
        assert len(response_data) > 0, f"Пустой ответ"

        response_item_id = None
        for item in response_data:
            if (item['bookingid'] == booking_id):
                response_item_id = item['bookingid']

        assert booking_id == response_item_id, f"Нет созданой записи"

        self.__delete_booking(auth_session, booking_id)

    def test_get_booking_by_checkout_date(self, auth_session, booking_data):
        # фильтрация запроса по датам

        booking_id = self.__create_booking(auth_session, booking_data)
        checkout = booking_data['bookingdates']['checkout']

        get_bookingIDs = auth_session.get(
            f"{BASE_URL}/booking/?checkout={checkout}")
        assert get_bookingIDs.status_code == 200, f"Ошибка получения записей"

        response_data = get_bookingIDs.json()
        assert len(response_data) > 0, f"Пустой ответ"

        response_item_id = None
        for item in response_data:
            if (item['bookingid'] == booking_id):
                response_item_id = item['bookingid']

        assert booking_id == response_item_id, f"Нет созданой записи"

        self.__delete_booking(auth_session, booking_id)
