import datetime
import logging

from dependency_injector.wiring import inject, Provide
from fastapi import Depends
from fastapi_events.handlers.local import local_handler
from fastapi_events.typing import Event

from app.conf.containers import Container
from app.security.business.services import SecurityService
from app.system.business.events import AuditLogEvents
from app.system.business.services import SystemService
from app.system.domain.models import AuditLog, AuditLogEventType

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@local_handler.register(event_name=AuditLogEvents.AUDIT_LOG_LOGGED)
@inject
def handle_audit_log_logged_events(event: Event,
                                   system_service: SystemService = Depends(Provide[Container.system_service]),
                                   security_service: SecurityService = Depends(Provide[Container.security_service])):
    event_name, payload = event
    try:
        logging.info(f"handle_audit_log_logged_events")
        log = AuditLog()
        log.source_no = payload
        log.logged_timestmap = datetime.datetime.now()
        log.event_type = AuditLogEventType.USER_CREATED
        log.user_id = 100 #100 security_service.get_current_user().id # 1001 #
        system_service.save_audit_log(log)
    except Exception as e:
        logging.error(f"Error {e.__cause__}")
