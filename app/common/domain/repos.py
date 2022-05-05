from typing import Optional, List, ContextManager

from sqlalchemy import and_, or_
from sqlalchemy.orm import Session

from app.common.domain.models import DistrictCode, StateCode


# ====================================================================================================
# DISTRICT CODE
# ====================================================================================================
class DistrictCodeRepository:
    def __init__(self, session_factory: ContextManager[Session]) -> None:
        self.session_factory = session_factory

    def find_by_id(self, id: int) -> Optional[DistrictCode]:
        with self.session_factory() as session:
            return session.get(DistrictCode, id)

    def find_by_code(self, code: str) -> DistrictCode:
        with self.session_factory() as session:
            return session.query(DistrictCode).filter(DistrictCode.code == code).first()

    def find(self) -> List[DistrictCode]:
        with self.session_factory() as session:
            return session.query(DistrictCode).all()

    def find(self, filter: str, offset: int, limit: int) -> List[DistrictCode]:
        with self.session_factory() as session:
            fltr = "%{}%".format(filter)
            query = session.query(DistrictCode).filter(
                or_(DistrictCode.code.like(fltr),
                    DistrictCode.description.like(fltr)))
            query.offset = offset
            query.limit = limit
            return query.all()

    def count(self) -> int:
        with self.session_factory() as session:
            return session.query(DistrictCode.id).count()

    def save(self, state_code: DistrictCode) -> None:
        with self.session_factory() as session:
            session.add(queue)
            session.commit()

    def update(self, state_code: DistrictCode) -> None:
        with self.session_factory() as session:
            session.refresh(queue)
            session.commit()

    def delete(self, state_code: DistrictCode) -> None:
        with self.session_factory() as session:
            session.delete(queue)
            session.commit()


# ====================================================================================================
# STATE CODE
# ====================================================================================================
class StateCodeRepository:
    def __init__(self, session_factory: ContextManager[Session]) -> None:
        self.session_factory = session_factory

    def find_by_id(self, id: int) -> Optional[StateCode]:
        with self.session_factory() as session:
            return session.get(StateCode, id)

    def find_by_code(self, code: str) -> StateCode:
        with self.session_factory() as session:
            return session.query(StateCode).filter(StateCode.code == code).first()

    def find(self) -> List[StateCode]:
        with self.session_factory() as session:
            return session.query(StateCode).all()

    def find(self, filter:str, offset: int, limit: int) -> List[StateCode]:
        with self.session_factory() as session:
            fltr = "%{}%".format(filter)
            query = session.query(StateCode).filter(
                or_(StateCode.code.like(fltr),
                    StateCode.description.like(fltr)))
            query.offset = offset
            query.limit = limit
            return query.all()

    def count(self) -> int:
        with self.session_factory() as session:
            return session.query(StateCode.id).count()

    def save(self, state_code: StateCode) -> None:
        with self.session_factory() as session:
            session.add(state_code)
            session.commit()

    def update(self, state_code: StateCode) -> None:
        with self.session_factory() as session:
            session.refresh(state_code)
            session.commit()

    def delete(self, state_code: StateCode) -> None:
        with self.session_factory() as session:
            session.delete(state_code)
            session.commit()
