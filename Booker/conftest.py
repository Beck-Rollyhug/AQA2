from faker import Faker
import requests
import pytest

from constant import BASE_URL, HEADERS, AUTH_JSON

faker = Faker()
AUTH_TOKEN = "YWRtaW46cGFzc3dvcmQxMjM="

@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    session.headers.update(HEADERS)
    session.headers.update({"Authorization": f"Basic {AUTH_TOKEN}"})
    response = requests.post(f"{BASE_URL}/auth", headers=HEADERS, json=AUTH_JSON)
    assert response.status_code == 200, f"auth error"
    token = response.json().get("token")
    assert token is not None, "no auth token"
    
    return session

@pytest.fixture()
def booking_data():
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

@pytest.fixture()
def booking_partial_update_data():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
    }