import logging
from typing import Optional, List, ContextManager

from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.identity.domain.models import User, Customer, Staff

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# ====================================================================================================
# USER
# ====================================================================================================
class UserRepository:
    def __init__(self, session_factory: ContextManager[Session]) -> None:
        self.session_factory = session_factory

    def find_by_id(self, user_id: int) -> Optional[User]:
        with self.session_factory() as session:
            return session.get(User, user_id)

    def find_by_username(self, username: str) -> User:
        with self.session_factory() as session:
            return session.query(User).filter(User.name == username).first()

    def find(self) -> List[User]:
        with self.session_factory() as session:
            return session.query(User).all()

    def find(self, offset: int, limit: int) -> List[User]:
        with self.session_factory() as session:
            query = session.query(User)
            query.offset(offset)
            query.limit(limit)
            return query.all()

    def save(self, user: User) -> User:
        with self.session_factory() as session:
            session.add(user)
            session.commit()
            return user

    def update(self, user: User) -> None:
        with self.session_factory() as session:
            session.refresh(user)
            session.commit()

    def delete(self, user: User) -> None:
        with self.session_factory() as session:
            session.delete(user)
            session.commit()


# ====================================================================================================
# STAFF
# ====================================================================================================
class StaffRepository:
    def __init__(self, session_factory: ContextManager[Session]) -> None:
        self.session_factory = session_factory

    def find_by_id(self, staff_id: int) -> Optional[Staff]:
        with self.session_factory() as session:
            return session.get(Staff, staff_id)

    def find_by_identity_no(self, identity_no: str) -> Staff:
        with self.session_factory() as session:
            return session.query(Staff).filter(Staff.identity_no == identity_no).first()

    def find(self) -> List[Staff]:
        with self.session_factory() as session:
            return session.query(Staff).all()

    def find(self, offset: int, limit: int) -> List[Staff]:
        with self.session_factory() as session:
            query = session.query(Staff)
            query.offset = offset
            query.limit = limit
            return query.all()

    def count(self) -> int:
        with self.session_factory() as session:
            return session.query(Staff.id).count()

    def save(self, staff: Staff) -> Staff:
        with self.session_factory() as session:
            session.add(staff)
            session.commit()
            return staff

    def update(self, staff: Staff) -> None:
        with self.session_factory() as session:
            session.refresh(staff)
            session.commit()

    def delete(self, staff: Staff) -> None:
        with self.session_factory() as session:
            session.delete(staff)
            session.commit()


# ====================================================================================================
# CUSTOMER
# ====================================================================================================
class CustomerRepository:
    def __init__(self, session_factory: ContextManager[Session]) -> None:
        self.session_factory = session_factory

    def find_by_id(self, customer_id: int) -> Optional[Customer]:
        with self.session_factory() as session:
            return session.get(Customer, customer_id)

    def find_by_identity_no(self, identity_no: str) -> Customer:
        with self.session_factory() as session:
            return session.query(Customer).filter(Customer.identity_no == identity_no).first()

    def find(self, filter: str, offset: int, limit: int) -> List[Customer]:
        fltr = "%{}%".format(filter)
        logging.debug(fltr)
        with self.session_factory() as session:
            return session.query(Customer).filter(
                or_(Customer.name.like(fltr), Customer.identity_no.like(fltr))).all()

    def count(self, filter: str) -> int:
        with self.session_factory() as session:
            fltr = "%{}%".format(filter)
            return session.query(Customer.id).filter(
                or_(Customer.name.like(fltr), Customer.identity_no.like(fltr))).count()

    def save(self, customer: Customer) -> Customer:
        with self.session_factory() as session:
            session.add(customer)
            session.commit()
            return customer

    def update(self, customer: Customer) -> None:
        with self.session_factory() as session:
            session.refresh(customer)
            session.commit()

    def delete(self, customer: Customer) -> None:
        with self.session_factory() as session:
            session.delete(customer)
            session.commit()
