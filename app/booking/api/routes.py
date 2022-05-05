import logging
from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.conf.containers import Container
from app.core.api.vos import ApplicationSuccess
from app.booking.business.services import BookingService
from app.booking.api import vos
from app.booking.domain import models
from app.identity.business.services import IdentityService

logger = logging.getLogger(__name__)

router = APIRouter(tags=["Booking"])


@router.get("/venues")
@inject
def find_venues(booking_service: BookingService = Depends(Provide[Container.booking_service])) -> List[vos.Venue]:
    logger.info("find_venues")
    return booking_service.find_venues()


@router.get("/venues/{code}")
@inject
def find_venue_by_code(code: str,
                       booking_service: BookingService = Depends(Provide[Container.booking_service])) -> vos.Venue:
    logger.info("find_venue by code")
    return booking_service.find_venue_by_code(code)


@router.post("/venues")
@inject
def save_venue(vo: vos.Venue,
               booking_service: BookingService = Depends(Provide[Container.booking_service])) -> ApplicationSuccess:
    logger.debug("save venue")
    venue = models.Venue()
    venue.code = vo.code
    venue.name = vo.name
    venue.description = vo.description
    venue.venue_type = models.VenueType(vo.venue_type.value)
    booking_service.save_venue(venue)
    return ApplicationSuccess.SUCCESS("Venue added")


@router.get("/reservation-applications")
@inject
def find_reservation_applications(booking_service: BookingService = Depends(Provide[Container.booking_service])) -> \
        List[vos.ReservationApplication]:
    return booking_service.find_reservation_applications()


@router.post("/reservation-applications/register")
@inject
def register_reservation_application(vo: vos.ReservationApplicationRegistration,
                                     booking_service: BookingService = Depends(Provide[Container.booking_service]),
                                     identity_service: IdentityService = Depends(Provide[Container.identity_service])
                                     ) -> ApplicationSuccess:
    logger.debug("save reservation")
    application = models.ReservationApplication()
    application.description = vo.description
    application.from_date = vo.from_date
    application.to_date = vo.to_date
    application.customer = identity_service.find_customer_by_identity_no(vo.customer)
    application.venue = booking_service.find_venue_by_code(vo.venue)
    application.application_status = models.ReservationApplicationStatus.REGISTERED
    reference_no = booking_service.register_reservation_application(application)
    return ApplicationSuccess.SUCCESS_WITH_RESULT("Application added", reference_no)


@router.post("/reservation-applications/{reference_no}/check")
@inject
def check_reservation_application(reference_no: str,
                                  booking_service: BookingService = Depends(Provide[Container.booking_service])
                                  ) -> ApplicationSuccess:
    application = booking_service.find_reservation_application_by_reference_no(reference_no)
    booking_service.check_reservation_application(application)
    return ApplicationSuccess.SUCCESS("Application checked")


@router.post("/reservation-applications/{reference_no}/approve")
@inject
def approve_reservation_application(reference_no: str,
                                    booking_service: BookingService = Depends(Provide[Container.booking_service])
                                    ) -> ApplicationSuccess:
    application = booking_service.find_reservation_application_by_reference_no(reference_no)
    booking_service.approve_reservation_application(application)
    return ApplicationSuccess.SUCCESS("Application approved")


@router.post("/reservation-applications/{reference_no}/reject")
@inject
def reject_reservation_application(reference_no: str,
                                   booking_service: BookingService = Depends(Provide[Container.booking_service])
                                   ) -> ApplicationSuccess:
    application = booking_service.find_reservation_application_by_reference_no(reference_no)
    booking_service.reject_reservation_application(application)
    return ApplicationSuccess.SUCCESS("Application rejected")
