import datetime
import logging
from typing import List, ContextManager
from uuid import uuid4

from sqlalchemy.orm import Session

from app.system.domain.models import SequenceGenerator, EmailQueue, EmailTemplate, AuditLog
from app.system.domain.repos import EmailTemplateRepository, EmailQueueRepository, SequenceGeneratorRepository, \
    AuditLogRepository

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class SystemService:

    def __init__(self,
                 email_template_repository: EmailTemplateRepository,
                 email_queue_repository: EmailQueueRepository,
                 sequence_generator_repository: SequenceGeneratorRepository,
                 audit_log_repository: AuditLogRepository,
                 session_factory: ContextManager[Session]) -> None:
        logger.debug(f"SystemService")
        self.email_template_repository: EmailTemplateRepository = email_template_repository
        self.email_queue_repository: EmailQueueRepository = email_queue_repository
        self.sequence_generator_repository: SequenceGeneratorRepository = sequence_generator_repository
        self.audit_log_repository: AuditLogRepository = audit_log_repository
        self.session_factory = session_factory
        super().__init__()

    # ====================================================================================================
    # EMAIL TEMPLATE
    # ====================================================================================================

    def find_email_template_by_code(self, code: str) -> EmailTemplate:
        template = self.email_template_repository.find_by_code(code)
        # dispatch(SystemEvents.USER_VIEWED, payload=user)
        return template

    def find_email_templates(self) -> List[EmailTemplate]:
        logger.debug(f"find_email_templates")
        templates = self.email_template_repository.find()
        return templates

    def save_email_template(self, template: EmailTemplate) -> None:
        logger.debug(f"save_email_template")
        with self.session_factory() as session:
            self.email_template_repository.save(template)
            session.flush()
            # dispatch(SystemEvents.USER_SAVED, payload=user)

    # ====================================================================================================
    # EMAIL QUEUE
    # ====================================================================================================

    def find_email_queue_by_code(self, code: str) -> EmailQueue:
        queue = self.email_queue_repository.find_by_code(code)
        # dispatch(SystemEvents.USER_VIEWED, payload=user)
        return queue

    def find_email_queues(self) -> List[EmailQueue]:
        logger.debug(f"find_email_queues")
        queues = self.email_queue_repository.find()
        return queues

    def save_email_queue(self, queue: EmailQueue) -> None:
        logger.debug(f"save_email_queue")
        with self.session_factory() as session:
            self.email_queue_repository.save(queue)
            session.flush()
            # dispatch(SystemEvents.USER_SAVED, payload=user)

    # ====================================================================================================
    # SEQUENCE GENERATOR
    # ====================================================================================================

    def find_sequence_generator_by_code(self, code: str) -> SequenceGenerator:
        user = self.sequence_generator_repository.find_by_code(code)
        # dispatch(SystemEvents.USER_VIEWED, payload=user)
        return user

    def find_sequence_generators(self) -> List[SequenceGenerator]:
        logger.debug(f"find_sequence_generators")
        generators = self.sequence_generator_repository.find()
        return generators

    def save_sequence_generator(self, generator: SequenceGenerator) -> None:
        logger.debug(f"save_sequence_generator")
        with self.session_factory() as session:
            self.sequence_generator_repository.save(generator)
            session.flush()
            # dispatch(SystemEvents.USER_SAVED, payload=user)

    #  [a] = prefix
    #  [b] = long year
    #  [c] = short year
    #  [d] = long month
    #  [e] = short month
    #  [f] = long day
    #  [g] = short day
    #  [h] = long hour  (24)
    #  [i] = short hour
    #  [j] = sequence
    # context.setVariable(PREFIX, sequenceGenerator.getPrefix());
    # context.setVariable(LONG_YEAR_FORMAT.toPattern(), LONG_YEAR_FORMAT.format(now));
    # context.setVariable(SHORT_YEAR_FORMAT.toPattern(), SHORT_YEAR_FORMAT.format(now));
    # context.setVariable(LONG_MONTH_FORMAT.toPattern(), LONG_MONTH_FORMAT.format(now));
    # context.setVariable(SHORT_MONTH_FORMAT.toPattern(), SHORT_MONTH_FORMAT.format(now));
    # context.setVariable(LONG_DAY_FORMAT.toPattern(), LONG_DAY_FORMAT.format(now));
    # context.setVariable(SHORT_DAY_FORMAT.toPattern(), SHORT_DAY_FORMAT.format(now));
    # context.setVariable(LONG_HOUR_FORMAT.toPattern(), LONG_HOUR_FORMAT.format(now));
    # context.setVariable(SHORT_HOUR_FORMAT.toPattern(), SHORT_HOUR_FORMAT.format(now));
    # context.setVariable(SEQUENCE, numberFormat.format(oldValue));
    def generate_formatted_sequence(self, code: str) -> str:
        logger.debug(f"generate_formatted_sequence")
        generated = ""
        with self.session_factory() as session:
            now = datetime.datetime.now()
            generator = self.sequence_generator_repository.find_by_code(code)

            new_value = generator.current_value + generator.increment_value
            generator.current_value = new_value
            self.sequence_generator_repository.update(generator)
            session.flush()

            generated = generator.reference_format
            generated.replace("#a", generator.prefix)
            generated.replace("#b", generator.prefix)
            generated.replace("#c", generator.prefix)
            generated.replace("#d", generator.prefix)
            generated.replace("#e", generator.prefix)
            generated.replace("#f", generator.prefix)
            generated.replace("#g", generator.prefix)
            generated.replace("#h", generator.prefix)
            generated.replace("#i", generator.prefix)
            generated.replace("#j", generator.prefix)
            generated.replace("#k", generator.prefix)
            generated.replace("#j", generator.sequence_format)
            return generated

    def generate_uuid(self) -> str:
        logger.debug(f"generate_uuid")
        return str(uuid4())

    # ====================================================================================================
    # EMAIL TEMPLATE
    # ====================================================================================================

    def find_audit_logs(self) -> List[AuditLog]:
        logger.debug(f"find_audit_logs")
        templates = self.audit_log_repository.find()
        return templates

    def save_audit_log(self, template: AuditLog) -> None:
        logger.debug(f"save_audit_log")
        with self.session_factory() as session:
            self.audit_log_repository.save(template)
            session.flush()


