import logging
from contextlib import contextmanager
from typing import ContextManager

from app.identity.domain.models import User

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class SecurityContext:
    def __init__(self) -> None:
        logger.debug(f"SecurityContext.__init__")

    def set(self, current_user: User):
        self.current_user = current_user

    @contextmanager
    def current_user(self) -> ContextManager[User]:
        curr_user = self.current_user
        try:
            yield curr_user
        except Exception:
            raise
        finally:
            pass
#
