from enum import Enum
from typing import Optional, List

from datetime import date, datetime
from pydantic import BaseModel

from app.identity.api.vos import Customer


class VenueType(Enum):
    HALL = 1
    ROOM = 2
    SPACE = 2


class Venue(BaseModel):
    id: Optional[int]
    code: str
    name: str
    description: str
    venue_type: VenueType

    class Config:
        orm_mode = True


class VenueResult(BaseModel):

    def __init__(cls, data: List[Venue], page: int, total_record: int) -> None:
        super().__init__(data=data, page=page, total_record=total_record)

    data: List[Venue] = []
    page: int = 0
    total_record: int = 0


class ReservationApplicationStatus(Enum):
    REGISTERED = 1
    CHECKED = 2
    APPROVED = 3
    REJECTED = 4


class ReservationApplicationRegistration(BaseModel):
    description: str
    customer: str
    venue: str
    from_date: datetime
    to_date: datetime


class ReservationApplication(BaseModel):
    id: Optional[int]
    reference_no: Optional[str]
    description: str
    from_date: datetime
    to_date: datetime
    application_status: ReservationApplicationStatus
    customer: Customer
    venue: Venue

    class Config:
        orm_mode = True


class ReservationApplicationResult(BaseModel):

    def __init__(cls, data: List[ReservationApplication], page: int, total_record: int) -> None:
        super().__init__(data=data, page=page, total_record=total_record)

    data: List[ReservationApplication] = []
    page: int = 0
    total_record: int = 0


class ReservationStatus(Enum):
    RESERVED = 1
    CANCELLED = 2


class Reservation(BaseModel):
    id: Optional[int]
    source_no: str
    from_date: datetime
    to_date: datetime
    reservation_status: ReservationStatus
    customer: Customer
    venue: Venue

    class Config:
        orm_mode = True


class ReservationApplicationResult(BaseModel):

    def __init__(cls, data: List[Reservation], page: int, total_record: int) -> None:
        super().__init__(data=data, page=page, total_record=total_record)

    data: List[Reservation] = []
    page: int = 0
    total_record: int = 0
