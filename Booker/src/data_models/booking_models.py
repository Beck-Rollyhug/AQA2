from pydantic import BaseModel
from datetime import date


class BookingDates(BaseModel):
    checkin: date
    checkout: date


class BookingData(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str


class BookingResponseCreate(BaseModel):
    bookingid: int
    booking: BookingData


class BookingResponseGetItems(BaseModel):
    bookingid: int
