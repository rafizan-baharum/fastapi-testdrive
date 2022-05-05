# https://fastapi-utils.davidmontague.xyz/user-guide/class-based-views/
# get_jwt_user
import logging
from typing import List, ContextManager

from fastapi_events.dispatcher import dispatch
from sqlalchemy.orm import Session

from app.identity.business.events import CustomerEvents
from app.identity.domain.models import User, Customer, Staff
from app.identity.domain.repos import UserRepository, CustomerRepository, StaffRepository
from app.system.business.events import AuditLogEvents

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class IdentityService:

    def __init__(self,
                 user_repository: UserRepository,
                 staff_repository: StaffRepository,
                 customer_repository: CustomerRepository,
                 session_factory: ContextManager[Session]) -> None:
        logger.debug(f"IdentityService")
        self.user_repository: UserRepository = user_repository
        self.staff_repository: StaffRepository = staff_repository
        self.customer_repository: CustomerRepository = customer_repository
        self.session_factory = session_factory
        super().__init__()

    # ====================================================================================================
    # USER
    # ====================================================================================================

    def find_user_by_username(self, username: str) -> User:
        user = self.user_repository.find_by_username(username)
        # dispatch(UserEvents.USER_VIEWED, payload=user)
        return user

    def find_users(self) -> List[User]:
        logger.debug(f"find_users")
        users = self.user_repository.find()
        return users

    def find_users(self, offset: int, limit: int) -> List[User]:
        logger.debug(f"find_users")
        users = self.user_repository.find(offset, limit)
        return users

    def save_user(self, user: User) -> None:
        logger.debug(f"save_user")
        with self.session_factory() as session:
            self.user_repository.save(user)
            session.flush()
            logger.debug(f"Id {user}")
            dispatch(UserEvents.USER_SAVED, payload=user)

    # ====================================================================================================
    # STAFF
    # ====================================================================================================
    def find_staff_by_identity_no(self, identity_no: str) -> Staff:
        staff = self.staff_repository.find_by_identity_no(identity_no)
        # dispatch(StaffEvents.STAFF_VIEWED, payload=staff)
        return staff

    def find_staffs(self) -> List[Staff]:
        logger.debug(f"find_staffs")
        staffs = self.staff_repository.find()
        return staffs

    def find_staffs(self, offset: int, limit: int) -> List[Staff]:
        logger.debug(f"find_staffs")
        staffs = self.staff_repository.find()
        return staffs

    def count_staff(self) -> int:
        staffs = self.staff_repository.count()
        return staffs

    def save_staff(self, staff: Staff) -> None:
        logger.debug(f"save_staff")
        with self.session_factory() as session:
            self.staff_repository.save(staff)
            session.flush()
            logger.debug(f"Id {staff}")
            # dispatch(StaffEvents.STAFF_SAVED, payload=staff)

    # ====================================================================================================
    # CUSTOMER
    # ====================================================================================================
    def find_customer_by_identity_no(self, identity_no: str) -> Customer:
        customer = self.customer_repository.find_by_identity_no(identity_no)
        return customer

    def find_customers(self, filter: str, offset: int, limit: int) -> List[Customer]:
        logger.debug(f"find_customers")
        customers = self.customer_repository.find(filter, offset, limit)
        return customers

    def count_customer(self, filter: str) -> int:
        logger.debug(f"count_customer")
        count = self.customer_repository.count(filter)
        return count

    def save_customer(self, customer: Customer) -> None:
        logger.info(f"save_customer")
        with self.session_factory() as session:
            self.customer_repository.save(customer)
            session.flush()
            dispatch(CustomerEvents.CUSTOMER_SAVED, payload=customer)
            dispatch(AuditLogEvents.AUDIT_LOG_LOGGED, payload='Customer is saved')
