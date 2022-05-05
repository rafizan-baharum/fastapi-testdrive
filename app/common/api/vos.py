from typing import Optional, List

from pydantic import BaseModel

from app.core.api.vos import MetaModel


class DistrictCode(MetaModel, BaseModel):
    id: Optional[int]
    code: str
    description: str

    class Config:
        orm_mode = True


class DistrictCodeResult(BaseModel):

    def __init__(cls, data: List[DistrictCode], page: int, total_record: int) -> None:
        super().__init__(data=data, page=page, total_record=total_record)

    data: List[DistrictCode] = []
    page: int = 0
    total_record: int = 0


class StateCode(MetaModel, BaseModel):
    id: Optional[int]
    code: str
    description: str

    class Config:
        orm_mode = True


class StateCodeResult(BaseModel):

    def __init__(cls, data: List[StateCode], page: int, total_record: int) -> None:
        super().__init__(data=data, page=page, total_record=total_record)

    data: List[StateCode] = []
    page: int = 0
    total_record: int = 0
