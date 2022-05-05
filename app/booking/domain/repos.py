from typing import Optional, List, ContextManager

from sqlalchemy.orm import Session

from app.booking.domain.models import Venue, ReservationApplication

# ====================================================================================================
# VENUE
# ====================================================================================================
class VenueRepository:
    def __init__(self, session_factory: ContextManager[Session]) -> None:
        self.session_factory = session_factory

    def find_by_id(self, venue_id: int) -> Optional[Venue]:
        with self.session_factory() as session:
            return session.get(Venue, venue_id)

    def find_by_code(self, code: str) -> Venue:
        with self.session_factory() as session:
            return session.query(Venue).filter(Venue.code == code).first()

    def find(self) -> List[Venue]:
        with self.session_factory() as session:
            return session.query(Venue).all()

    def count(self) -> int:
        with self.session_factory() as session:
            return session.query(Venue.id).count()

    def save(self, venue: Venue) -> None:
        with self.session_factory() as session:
            session.add(venue)
            session.commit()

    def update(self, Venue: Venue) -> None:
        with self.session_factory() as session:
            session.refresh(Venue)
            session.commit()

    def delete(self, Venue: Venue) -> None:
        with self.session_factory() as session:
            session.delete(Venue)
            session.commit()


# ====================================================================================================
# RESERVATION APPLICATION
# ====================================================================================================
class ReservationApplicationRepository:
    def __init__(self, session_factory: ContextManager[Session]) -> None:
        self.session_factory = session_factory

    def find_by_id(self, id: int) -> Optional[ReservationApplication]:
        with self.session_factory() as session:
            return session.get(ReservationApplication, id)

    def find_by_reference_no(self, reference_no: str) -> ReservationApplication:
        with self.session_factory() as session:
            return session.query(ReservationApplication).filter(
                ReservationApplication.reference_no == reference_no).first()

    def find(self) -> List[ReservationApplication]:
        with self.session_factory() as session:
            return session.query(ReservationApplication).all()

    def count(self) -> int:
        with self.session_factory() as session:
            return session.query(ReservationApplication.id).count()

    def save(self, application: ReservationApplication) -> None:
        with self.session_factory() as session:
            session.add(application)
            session.commit()

    def update(self, application: ReservationApplication) -> None:
        with self.session_factory() as session:
            session.refresh(application)
            session.commit()

    def delete(self, application: ReservationApplication) -> None:
        with self.session_factory() as session:
            session.delete(application)
            session.commit()
