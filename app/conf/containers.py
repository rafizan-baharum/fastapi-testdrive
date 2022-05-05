import logging

from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Factory, Singleton
from fastapi.security import OAuth2PasswordBearer

from app.booking.business.services import BookingService
from app.booking.domain.repos import VenueRepository, ReservationApplicationRepository
from app.common.business.services import CommonService
from app.common.domain.repos import DistrictCodeRepository, StateCodeRepository
from app.conf.database import Database
from app.conf.security_context import SecurityContext
from app.identity.business.services import IdentityService
from app.identity.domain.repos import UserRepository, StaffRepository, CustomerRepository
from app.security.business.services import SecurityService
from app.system.business.services import SystemService
from app.system.domain.repos import EmailTemplateRepository, EmailQueueRepository, SequenceGeneratorRepository, \
    AuditLogRepository

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Container(DeclarativeContainer):
    wiring_config = WiringConfiguration(
        modules=[
            "app.identity.api.routes",
            "app.identity.business.handlers",
            "app.booking.api.routes",
            "app.common.api.routes",
            "app.system.api.routes",
            "app.system.business.handlers",
            "app.security.api.routes",
            "app.tests.seed.seed",
            "app.conf.middlewares"
        ])
    # config = Configuration(yaml_files=["config.yml"])
    # logger.debug(f"db config {config.db.url}")
    db = Singleton(Database, db_url="postgresql://fa_test:fa_test@127.0.0.1/fa_test")
    # security_context = Singleton(SecurityContext)
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    # common
    district_code_repository = Factory(
        DistrictCodeRepository,
        session_factory=db.provided.session,
    )
    state_code_repository = Factory(
        StateCodeRepository,
        session_factory=db.provided.session,
    )
    common_service = Factory(
        CommonService,
        session_factory=db.provided.session,
        district_code_repository=district_code_repository,
        state_code_repository=state_code_repository,
    )

    # system
    email_template_repository = Factory(
        EmailTemplateRepository,
        session_factory=db.provided.session,
    )
    email_queue_repository = Factory(
        EmailQueueRepository,
        session_factory=db.provided.session,
    )
    sequence_generator_repository = Factory(
        SequenceGeneratorRepository,
        session_factory=db.provided.session,
    )
    audit_log_repository = Factory(
        AuditLogRepository,
        session_factory=db.provided.session,
    )
    system_service = Factory(
        SystemService,
        session_factory=db.provided.session,
        email_template_repository=email_template_repository,
        email_queue_repository=email_queue_repository,
        sequence_generator_repository=sequence_generator_repository,
        audit_log_repository=audit_log_repository,
    )

    # identity
    user_repository = Factory(
        UserRepository,
        session_factory=db.provided.session,
    )
    staff_repository = Factory(
        StaffRepository,
        session_factory=db.provided.session,
    )
    customer_repository = Factory(
        CustomerRepository,
        session_factory=db.provided.session,
    )
    identity_service = Factory(
        IdentityService,
        session_factory=db.provided.session,
        user_repository=user_repository,
        staff_repository=staff_repository,
        customer_repository=customer_repository,
    )

    security_service = Factory(
        SecurityService,
        session_factory=db.provided.session,
        user_repository=user_repository,
    )

    # booking
    venue_repository = Factory(
        VenueRepository,
        session_factory=db.provided.session,
    )
    reservation_application_repository = Factory(
        ReservationApplicationRepository,
        session_factory=db.provided.session,
    )
    booking_service = Factory(
        BookingService,
        session_factory=db.provided.session,
        reservation_application_repository=reservation_application_repository,
        venue_repository=venue_repository,
    )
