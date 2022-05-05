from typing import Optional, List

from pydantic import BaseModel

from app.core.api.vos import MetaModel


class EmailTemplate(MetaModel, BaseModel):
    id: Optional[int]
    code: str
    description: str
    subject: str
    template: str

    class Config:
        orm_mode = True


class EmailTemplateResult(BaseModel):

    def __init__(cls, data: List[EmailTemplate], page: int, total_record: int) -> None:
        super().__init__()

    data: List[EmailTemplate] = []
    page: int = 0
    total_record: int = 0


class EmailQueue(MetaModel, BaseModel):
    id: Optional[int]
    to: str
    cc: str
    bcc: str
    subject: str
    body: str
    error_message: str
    error_count: int

    class Config:
        orm_mode = True


class EmailQueueResult(BaseModel):

    def __init__(cls, data: List[EmailQueue], page: int, total_record: int) -> None:
        super().__init__()

    data: List[EmailQueue] = []
    page: int = 0
    total_record: int = 0


class SequenceGenerator(MetaModel, BaseModel):
    id: Optional[int]
    code: str
    description: str
    prefix: str
    sequence_format: str
    reference_format: str
    increment_value: int
    current_value: int

    class Config:
        orm_mode = True


class SequenceGeneratorResult(BaseModel):

    def __init__(cls, data: List[SequenceGenerator], page: int, total_record: int) -> None:
        super().__init__()

    data: List[SequenceGenerator] = []
    page: int = 0
    total_record: int = 0
