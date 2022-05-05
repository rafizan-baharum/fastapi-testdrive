import enum

from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, Date
from sqlalchemy.orm import relationship

from app.conf.database import Base
from app.core.domain.models import IntEnum, MetaObject
from app.identity.domain.models import Customer


class VenueType(enum.IntEnum):
    HALL = 1
    ROOM = 2
    SPACE = 3


class Venue(MetaObject, Base):
    __tablename__ = 'CNG_VENU'
    id = Column(Integer, Sequence('SQ_CNG_VENU'), primary_key=True)
    code = Column(String(50))
    name = Column(String(50))
    description = Column(String(200))
    venue_type = Column(IntEnum(VenueType), default=VenueType.HALL)

    __mapper_args__ = {
    }


class ReservationApplicationStatus(enum.IntEnum):
    REGISTERED = 1
    CHECKED = 2
    APPROVED = 3
    REJECTED = 4


class ReservationApplication(MetaObject, Base):
    __tablename__ = 'CNG_RSVN_APLN'
    id = Column(Integer, Sequence('SQ_CNG_RSVN_APLN'), primary_key=True)
    reference_no = Column(String(50))
    description = Column(String(50))
    from_date = Column(Date())
    to_date = Column(Date())
    customer_id = Column(ForeignKey(Customer.id))
    customer = relationship(Customer, uselist=False, backref="customer")
    venue_id = Column(ForeignKey(Venue.id))
    venue = relationship(Venue, uselist=False, backref="venue")
    application_status = Column(IntEnum(ReservationApplicationStatus), default=ReservationApplicationStatus.REGISTERED)

    __mapper_args__ = {
    }


class ReservationStatus(enum.IntEnum):
    RESERVED = 1
    CANCELLED = 2


class Reservation(MetaObject, Base):
    __tablename__ = 'CNG_RSVN'
    id = Column(Integer, Sequence('SQ_CNG_RSVN'), primary_key=True)
    source_no = Column(String(50))
    from_date = Column(Date())
    to_date = Column(Date())
    customer_id = Column(ForeignKey(Customer.id))
    customer = relationship(Customer, uselist=False, backref="reserver")
    venue_id = Column(ForeignKey(Venue.id))
    venue = relationship(Venue, uselist=False, backref="reserved_venue")
    reservation_status = Column(IntEnum(ReservationStatus), default=ReservationStatus.RESERVED)

    __mapper_args__ = {
    }
