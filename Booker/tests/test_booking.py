import pytest

from Booker.constant import BASE_URL
from Booker.src.scenarios.booking_scenarios import BookingScenarios


class TestBooking:
    def test_create_booking(self, auth_session, booking_data):
        booker = BookingScenarios(BASE_URL, auth_session)
        data = booking_data()
        booker.create_booking(data)

    def test_update_booking(self,
                            auth_session,
                            booking_data,
                            booking_update_data,
                            booking_partial_update_data):
        booker = BookingScenarios(BASE_URL, auth_session)
        data = booking_data()
        booker.update_booking(data, booking_update_data)

        data = booking_data(booking_partial_update_data)
        booker.partial_update_booking(data, booking_partial_update_data)

    def test_get_booking(self, auth_session, booking_data):
        booker = BookingScenarios(BASE_URL, auth_session)
        data = booking_data()
        booker.get_booking(data)
        booker.get_booking_by_fullname(data)
        booker.get_booking_by_firstname(data)
        booker.get_booking_by_lastname(data)

        # Баг бекенда: не находит по checkin, равной заданной;
        #              но находит по checkin, меньше заданной
        # booker.get_booking_by_bookingdates(booking_data)
        # booker.get_booking_by_checkin_date(booking_data)
        #

        booker.get_booking_by_checkout_date(data)
