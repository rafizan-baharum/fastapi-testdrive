from datetime import date, datetime, time, timedelta
from typing import Optional

from pydantic import BaseModel


class ApplicationSuccess(BaseModel):
    status: str
    message: str
    result: Optional[str]

    @classmethod
    def SUCCESS_WITH_RESULT(cls, message: str, result: str):
        return cls(status="SUCCESS", message=message, result=result)

    @classmethod
    def SUCCESS(cls, message: str):
        return cls(status="SUCCESS", message=message, result=None)


class ApplicationError(BaseModel):
    status: str
    message: str

    @classmethod
    def OK(cls, message: str):
        return cls(status="ERROR", message=message)


class MetaModel(BaseModel):
    c_id: Optional[int]
    c_ts: Optional[datetime]
    m_id: Optional[int]
    m_ts: Optional[datetime]
    d_id: Optional[int]
    d_ts: Optional[datetime]
