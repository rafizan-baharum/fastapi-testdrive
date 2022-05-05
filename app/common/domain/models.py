from sqlalchemy import Column, Integer, String, Sequence, Text

from app.conf.database import Base
from app.core.domain.models import MetaObject


class StateCode(MetaObject, Base):
    __tablename__ = 'CNG_STTE_CODE'
    id = Column(Integer, Sequence('SQ_CNG_STTE_CODE'), primary_key=True)
    code = Column(String(50))
    description = Column(String(50))


class DistrictCode(MetaObject, Base):
    __tablename__ = 'CNG_DSTC_CODE'
    id = Column(Integer, Sequence('SQ_CNG_DSTC_CODE'), primary_key=True)
    code = Column(String(50))
    description = Column(String(50))
