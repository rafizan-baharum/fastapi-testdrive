from typing import Optional, List, ContextManager

from sqlalchemy.orm import Session

from app.system.domain.models import EmailTemplate, EmailQueue, SequenceGenerator, AuditLog


# ====================================================================================================
# EMAIL TEMPLATE
# ====================================================================================================

class EmailTemplateRepository:
    def __init__(self, session_factory: ContextManager[Session]) -> None:
        self.session_factory = session_factory

    def find_by_id(self, id: int) -> Optional[EmailTemplate]:
        with self.session_factory() as session:
            return session.get(EmailTemplate, id)

    def find_by_code(self, code: str) -> EmailTemplate:
        with self.session_factory() as session:
            return session.query(EmailTemplate).filter(EmailTemplate.code == code).first()

    def find(self) -> List[EmailTemplate]:
        with self.session_factory() as session:
            return session.query(EmailTemplate).all()

    def save(self, template: EmailTemplate) -> None:
        with self.session_factory() as session:
            session.add(template)
            session.commit()

    def update(self, template: EmailTemplate) -> None:
        with self.session_factory() as session:
            session.refresh(template)
            session.commit()

    def delete(self, template: EmailTemplate) -> None:
        with self.session_factory() as session:
            session.delete(template)
            session.commit()


# ====================================================================================================
# EMAIL QUEUE
# ====================================================================================================

class EmailQueueRepository:
    def __init__(self, session_factory: ContextManager[Session]) -> None:
        self.session_factory = session_factory

    def find_by_id(self, id: int) -> Optional[EmailQueue]:
        with self.session_factory() as session:
            return session.get(EmailQueue, id)

    def find(self) -> List[EmailQueue]:
        with self.session_factory() as session:
            return session.query(EmailQueue).all()

    def save(self, queue: EmailQueue) -> None:
        with self.session_factory() as session:
            session.add(queue)
            session.commit()

    def update(self, queue: EmailQueue) -> None:
        with self.session_factory() as session:
            session.refresh(queue)
            session.commit()

    def delete(self, queue: EmailQueue) -> None:
        with self.session_factory() as session:
            session.delete(queue)
            session.commit()


# ====================================================================================================
# SEQUENCE GENERATOR
# ====================================================================================================

class SequenceGeneratorRepository:
    def __init__(self, session_factory: ContextManager[Session]) -> None:
        self.session_factory = session_factory

    def find_by_id(self, id: int) -> Optional[SequenceGenerator]:
        with self.session_factory() as session:
            return session.get(SequenceGenerator, id)

    def find_by_code(self, code: str) -> SequenceGenerator:
        with self.session_factory() as session:
            return session.query(SequenceGenerator).filter(SequenceGenerator.code == code).first()

    def find(self) -> List[SequenceGenerator]:
        with self.session_factory() as session:
            return session.query(SequenceGenerator).all()

    def save(self, generator: SequenceGenerator) -> None:
        with self.session_factory() as session:
            session.add(generator)
            session.commit()

    def update(self, generator: SequenceGenerator) -> None:
        with self.session_factory() as session:
            session.refresh(generator)
            session.commit()

    def delete(self, generator: SequenceGenerator) -> None:
        with self.session_factory() as session:
            session.delete(generator)
            session.commit()


# ====================================================================================================
# SEQUENCE GENERATOR
# ====================================================================================================

class AuditLogRepository:
    def __init__(self, session_factory: ContextManager[Session]) -> None:
        self.session_factory = session_factory

    def find_by_id(self, id: int) -> Optional[AuditLog]:
        with self.session_factory() as session:
            return session.get(AuditLog, id)

    def find(self) -> List[AuditLog]:
        with self.session_factory() as session:
            return session.query(AuditLog).all()

    def save(self, generator: AuditLog) -> None:
        with self.session_factory() as session:
            session.add(generator)
            session.commit()

    def update(self, generator: AuditLog) -> None:
        with self.session_factory() as session:
            session.refresh(generator)
            session.commit()

    def delete(self, generator: AuditLog) -> None:
        with self.session_factory() as session:
            session.delete(generator)
            session.commit()
