import logging
from typing import List, ContextManager
from uuid import uuid4

from fastapi_events.dispatcher import dispatch
from sqlalchemy.orm import Session

from app.booking.business.events import ReservationApplicationEvents
from app.booking.domain.models import Venue, ReservationApplication, ReservationApplicationStatus
from app.booking.domain.repos import VenueRepository, ReservationApplicationRepository

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class BookingService:

    def __init__(self,
                 venue_repository: VenueRepository,
                 reservation_application_repository: ReservationApplicationRepository,
                 session_factory: ContextManager[Session]) -> None:
        logger.debug(f"BookingService")
        self.venue_repository: VenueRepository = venue_repository
        self.reservation_application_repository: ReservationApplicationRepository = reservation_application_repository
        self.session_factory = session_factory
        super().__init__()

    # ======================================================================================================
    # VENUE
    # ======================================================================================================

    def find_venue_by_code(self, code: str) -> Venue:
        venue = self.venue_repository.find_by_code(code)
        # dispatch(VenueEvents.VENUE_VIEWED, payload=venue)
        return venue

    def find_venues(self) -> List[Venue]:
        logger.debug(f"find_venues")
        venues = self.venue_repository.find()
        return venues

    def save_venue(self, venue: Venue) -> None:
        logger.debug(f"save_venue")
        with self.session_factory() as session:
            self.venue_repository.save(venue)
            session.flush()
            logger.debug(f"id {venue}")
            # dispatch(VenueEvents.VENUE_SAVED, payload=venue)

    # ======================================================================================================
    # RESERVATION APPLICATION
    # ======================================================================================================

    def find_reservation_application_by_reference_no(self, reference_no: str) -> ReservationApplication:
        reservation_application = self.reservation_application_repository.find_by_reference_no(reference_no)
        return reservation_application

    def find_reservation_applications(self) -> List[ReservationApplication]:
        logger.debug(f"find_reservation_applications")
        reservation_applications = self.reservation_application_repository.find()
        return reservation_applications

    def register_reservation_application(self, application: ReservationApplication) -> str:
        logger.debug(f"register_reservation_application")
        uid = uuid4()
        application.reference_no = f"{uid}"
        with self.session_factory() as session:
            self.reservation_application_repository.save(application)
            session.flush()

            dispatch(ReservationApplicationEvents.RESERVATION_APPLICATION_REGISTERED, payload=application)
        return str(uid)

    def check_reservation_application(self, application: ReservationApplication) -> None:
        with self.session_factory() as session:
            application.application_status = ReservationApplicationStatus.REGISTERED
            self.reservation_application_repository.update(application)
            session.flush()

            dispatch(ReservationApplicationEvents.RESERVATION_APPLICATION_CHECKED, payload=application)

    def approve_reservation_application(self, application: ReservationApplication) -> None:
        with self.session_factory() as session:
            application.application_status = ReservationApplicationStatus.APPROVED
            self.reservation_application_repository.update(application)
            session.flush()

            dispatch(ReservationApplicationEvents.RESERVATION_APPLICATION_APPROVED, payload=application)

    def reject_reservation_application(self, application: ReservationApplication) -> None:
        with self.session_factory() as session:
            application.application_status = ReservationApplicationStatus.REJECT
            self.reservation_application_repository.update(application)
            session.flush()

            dispatch(ReservationApplicationEvents.RESERVATION_APPLICATION_REJECT, payload=application)

    # ======================================================================================================
    # RESERVATION APPLICATION
    # ======================================================================================================

    def find_reservation_by_source_no(self, source_no: str) -> ReservationApplication:
        reservation_application = self.reservation_application_repository.find_by_source_no(source_no)
        return reservation_application

    def find_reservation_by_reservation_application(self,
                                                    application: ReservationApplication) -> ReservationApplication:
        reservation_application = self.reservation_application_repository.find_by_source_no(application.reference_no)
        return reservation_application

    def find_reservation_applications(self) -> List[ReservationApplication]:
        logger.debug(f"find_reservation_applications")
        reservation_applications = self.reservation_application_repository.find()
        return reservation_applications

    def find_reservation_applications(self) -> List[ReservationApplication]:
        logger.debug(f"find_reservation_applications")
        reservation_applications = self.reservation_application_repository.find()
        return reservation_applications

    def register_reservation_application(self, application: ReservationApplication) -> str:
        logger.debug(f"register_reservation_application")
        uid = uuid4()
        application.reference_no = f"{uid}"
        with self.session_factory() as session:
            self.reservation_application_repository.save(application)
            session.flush()
            # dispatch(VenueEvents.VENUE_SAVED, payload=venue)
        return str(uid)
