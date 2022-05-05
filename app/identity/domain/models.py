import enum

from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Sequence, TypeDecorator
from sqlalchemy.orm import relationship

from app.conf.database import Base
from app.core.domain.models import IntEnum, MetaObject


class PrincipalType(enum.IntEnum):
    USER = 1
    GROUP = 2


class Principal(MetaObject, Base):
    __tablename__ = 'CNG_PCPL'
    id = Column(Integer, Sequence('SQ_CNG_PCPL'), primary_key=True)
    name = Column(String(50), unique=True)
    principal_type = Column(IntEnum(PrincipalType), default=PrincipalType.USER)

    __mapper_args__ = {
        'polymorphic_identity': 'Principal',
        'polymorphic_on': principal_type
    }


class User(Principal):
    __tablename__ = 'CNG_USER'
    id = Column(Integer, ForeignKey('CNG_PCPL.id'), primary_key=True)
    password = Column(String(30))
    realname = Column(String(30))
    email = Column(String(30))

    __mapper_args__ = {
        'polymorphic_identity': PrincipalType.USER,
    }


class Group(Principal):
    __tablename__ = 'CNG_GROP'
    id = Column(Integer, ForeignKey('CNG_PCPL.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': PrincipalType.GROUP,
    }


class ActorType(enum.IntEnum):
    STAFF = 1
    CUSTOMER = 2


class Actor(MetaObject, Base):
    __tablename__ = 'CNG_ACTR'
    id = Column(Integer, Sequence('SQ_CNG_ACTR'), primary_key=True)
    identity_no = Column(String(50))
    name = Column(String(50))
    actor_type = Column(IntEnum(ActorType), default=ActorType.STAFF)
    user_id = Column(ForeignKey(User.id), nullable=True)
    user = relationship(User, uselist=False, backref="actor")

    __mapper_args__ = {
        'polymorphic_identity': 'Actor',
        'polymorphic_on': actor_type
    }


class Staff(Actor):
    __tablename__ = 'CNG_STAF'
    id = Column(Integer, ForeignKey('CNG_ACTR.id'), primary_key=True)
    department = Column(String(50))
    position = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': ActorType.STAFF,
    }


class Customer(Actor):
    __tablename__ = 'CNG_CSMR'
    id = Column(Integer, ForeignKey('CNG_ACTR.id'), primary_key=True)
    address = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': ActorType.CUSTOMER,
    }
