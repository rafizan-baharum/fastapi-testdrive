import enum

from sqlalchemy import Column, Integer, String, Sequence, Text, DateTime

from app.conf.database import Base
from app.core.domain.models import MetaObject, IntEnum


class EmailTemplate(MetaObject, Base):
    __tablename__ = 'CNG_EMIL_TMPL'
    id = Column(Integer, Sequence('SQ_CNG_EMIL_TMPL'), primary_key=True)
    code = Column(String(50))
    description = Column(String(50))
    subject = Column(String(50))
    template = Column(Text())


class EmailQueue(MetaObject, Base):
    __tablename__ = 'CNG_EMIL_QUEU'
    id = Column(Integer, Sequence('SQ_CNG_EMIL_QUEU'), primary_key=True)
    to = Column(String(50))
    cc = Column(String(50))
    bcc = Column(String(50))
    subject = Column(String(50))
    body = Column(String(50))
    error_message = Column(String(50))
    error_count = Column(String(50))


class SequenceGenerator(MetaObject, Base):
    __tablename__ = 'CNG_SQNC_GNTR'
    id = Column(Integer, Sequence('SQ_CNG_SQNC_GNTR'), primary_key=True)
    code = Column(String(50))
    description = Column(String(50))
    prefix = Column(String(50))
    sequence_format = Column(String(50))
    reference_format = Column(String(50))
    increment_value = Column(Integer())
    current_value = Column(Integer())


class AuditLogEventType(enum.IntEnum):
    NONE = 0
    USER_CREATED = 1
    USER_DELETED = 2


class AuditLog(MetaObject, Base):
    __tablename__ = 'CNG_AUDT_LOG'
    id = Column(Integer, Sequence('SQ_CNG_AUDT_LOG'), primary_key=True)
    user_id = Column(Integer)
    logged_timestmap = Column(DateTime())
    source_no = Column(String(50))
    event_type = Column(IntEnum(AuditLogEventType), default=AuditLogEventType.NONE)
