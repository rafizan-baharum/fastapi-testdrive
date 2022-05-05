import logging
import threading
from typing import ContextManager

from sqlalchemy.orm import Session

from app.identity.domain.models import User
from app.identity.domain.repos import UserRepository

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class SecurityService:

    def __init__(self,
                 user_repository: UserRepository,
                 session_factory: ContextManager[Session],
                 ) -> None:
        logger.debug(f"SecurityService")
        self.user_repository: UserRepository = user_repository
        self.session_factory = session_factory
        super().__init__()

    # ====================================================================================================
    # SECURITY
    # ====================================================================================================

    def get_current_user(self) -> User:
        # logger.info(f"thread data: {thread_data}")
        # logger.info(f"user: {thread_data.current_user}")
        return None
