from enum import Enum
from typing import Optional, List, Any

from pydantic import BaseModel


class PrincipalType(Enum):
    USER = 1
    GROUP = 2


class Principal(BaseModel):
    id: Optional[int]
    name: str
    principal_type: PrincipalType

    class Config:
        orm_mode = True


class User(Principal):
    realname: str
    email: str
    password: str

    class Config:
        orm_mode = True


class UserResult(BaseModel):

    def __init__(cls, data: List[User], page: int, total_record: int) -> None:
        super().__init__(data=data, page=page, total_record=total_record)

    data: List[User] = []
    page: int = 0
    total_record: int = 0


class Group(Principal):
    class Config:
        orm_mode = True


class GroupResult(BaseModel):

    def __init__(cls, data: List[Group], page: int, total_record: int) -> None:
        super().__init__(data=data, page=page, total_record=total_record)

    data: List[Group] = []
    page: int = 0
    total_record: int = 0


class ActorType(Enum):
    STAFF = 1
    CUSTOMER = 2


class Actor(BaseModel):
    id: Optional[int]
    identity_no: str
    name: str
    actor_type: ActorType

    class Config:
        orm_mode = True


class Staff(Actor):
    department: str
    position: str

    class Config:
        orm_mode = True


class StaffResult(BaseModel):

    def __init__(cls, data: List[Staff], page: int, total_record: int) -> None:
        super().__init__(data=data, page=page, total_record=total_record)

    data: List[Staff] = []
    page: int = 0
    total_record: int = 0


class Customer(Actor):
    address: str

    class Config:
        orm_mode = True


class CustomerResult(BaseModel):
    data: List[Customer]
    page: int
    total_record: int

    def __init__(cls, data: List[Customer], page: int, total_record: int) -> None:
        super().__init__(data=data, page=page, total_record=total_record)
