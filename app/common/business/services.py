import logging
from typing import List, ContextManager

from sqlalchemy.orm import Session

from app.common.domain.models import StateCode
from app.common.domain.repos import DistrictCodeRepository, StateCodeRepository
from app.identity.domain.models import User

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class CommonService:

    def __init__(self,
                 district_code_repository: DistrictCodeRepository,
                 state_code_repository: StateCodeRepository,
                 session_factory: ContextManager[Session]) -> None:
        logger.debug(f"SystemService")
        self.district_code_repository: DistrictCodeRepository = district_code_repository
        self.state_code_repository: StateCodeRepository = state_code_repository
        self.session_factory = session_factory
        super().__init__()

    # ====================================================================================================
    # DISTRICT CODE
    # ====================================================================================================

    def find_district_code_by_code(self, code: str) -> User:
        user = self.district_code_repository.find_by_code(code)
        # dispatch(UserEvents.USER_VIEWED, payload=user)
        return user

    def find_district_codes(self, filter: str, offset: int, limit: int) -> List[User]:
        logger.debug(f"find_district_codes")
        users = self.district_code_repository.find(filter, offset, limit)
        return users

    def save_district_code(self, user: User) -> None:
        logger.debug(f"save_district_code")
        with self.session_factory() as session:
            self.district_code_repository.save(user)
            session.flush()
            # dispatch(UserEvents.USER_SAVED, payload=user)

    # ====================================================================================================
    # STATE CODE
    # ====================================================================================================

    def find_state_code_by_code(self, code: str) -> User:
        user = self.state_code_repository.find_by_code(code)
        # dispatch(UserEvents.USER_VIEWED, payload=user)
        return user

    def find_state_codes(self, filter: str, offset: int, limit: int) -> List[User]:
        logger.debug(f"find_state_codes")
        users = self.state_code_repository.find(filter, offset, limit)
        return users

    def save_state_code(self, state_code: StateCode) -> None:
        logger.debug(f"save_state_code")
        with self.session_factory() as session:
            self.state_code_repository.save(state_code)
            session.flush()
            # dispatch(UserEvents.USER_SAVED, payload=user)
