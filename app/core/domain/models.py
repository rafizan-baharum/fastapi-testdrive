import enum

from sqlalchemy import TypeDecorator, Integer, Column, DateTime


class IntEnum(TypeDecorator):
    """
    Enables passing in a Python enum and storing the enum's *value* in the db.
    The default would have stored the enum's *name* (ie the string).
    """
    impl = Integer

    def __init__(self, enumtype, *args, **kwargs):
        super(IntEnum, self).__init__(*args, **kwargs)
        self._enumtype = enumtype

    def process_bind_param(self, value, dialect):
        if isinstance(value, int):
            return value

        return value.value

    def process_result_value(self, value, dialect):
        return self._enumtype(value)


class MetaState(enum.IntEnum):
    INACTIVE = 0
    ACTIVE = 1


class MetaObject(object):
    m_st = Column(IntEnum(MetaState), default=MetaState.ACTIVE)
    c_id = Column(Integer, nullable=True)
    c_ts = Column(DateTime, nullable=True)
    m_id = Column(Integer, nullable=True)
    m_ts = Column(DateTime, nullable=True)
    d_id = Column(Integer, nullable=True)
    d_ts = Column(DateTime, nullable=True)
