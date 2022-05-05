import logging

from fastapi_events.dispatcher import dispatch
from fastapi_events.handlers.local import local_handler
from fastapi_events.typing import Event

from app.identity.business.events import CustomerEvents
from app.system.business.events import AuditLogEvents

logger = logging.getLogger("root")
logger.setLevel(logging.INFO)

@local_handler.register(event_name=CustomerEvents.CUSTOMER_VIEWED)
def handle_customer_viewed_events(event: Event):
    event_name, payload = event
    logging.debug(event_name)

@local_handler.register(event_name=CustomerEvents.CUSTOMER_SAVED)
def handle_customer_saved_events(event: Event):
    event_name, payload = event
    logging.debug(event_name)
