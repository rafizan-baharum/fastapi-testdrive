import logging

from fastapi_events.handlers.local import local_handler
from fastapi_events.typing import Event

from app.booking.business.events import ReservationApplicationEvents

logger = logging.getLogger("root")
logger.setLevel(logging.INFO)


@local_handler.register(event_name=ReservationApplicationEvents.RESERVATION_APPLICATION_REGISTERED)
def handle_registered_events(event: Event):
    event_name, payload = event
    logging.debug(event_name)


@local_handler.register(event_name=ReservationApplicationEvents.RESERVATION_APPLICATION_CHECKED)
def handle_checked_events(event: Event):
    event_name, payload = event
    logging.debug(event_name)


@local_handler.register(event_name=ReservationApplicationEvents.RESERVATION_APPLICATION_APPROVED)
def handle_approved_events(event: Event):
    event_name, payload = event
    logging.debug(event_name)


@local_handler.register(event_name=ReservationApplicationEvents.RESERVATION_APPLICATION_REJECTED)
def handle_rejected_events(event: Event):
    event_name, payload = event
    logging.debug(event_name)
