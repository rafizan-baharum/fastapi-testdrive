import logging
from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.conf.containers import Container
from app.core.api.vos import ApplicationSuccess
from app.core.constants import LIMIT
from app.identity.api import vos
from app.identity.api.vos import StaffResult, CustomerResult
from app.identity.business.services import IdentityService
from app.identity.domain import models
from app.security.api.routes import get_current_user
from app.security.api.vos import AuthorizedUser

logger = logging.getLogger(__name__)

router = APIRouter(tags=["Identity"])


# ====================================================================================================
# USER
# ====================================================================================================

@router.get("/users")
@inject
def find_users(identity_service: IdentityService = Depends(Provide[Container.identity_service]),
               token: str = Depends(Container.oauth2_scheme)
               ) -> List[vos.User]:
    logger.info("find_users")
    return identity_service.find_users()


@router.get("/users/{username}")
@inject
def find_user_by_username(username: str,
                          identity_service: IdentityService = Depends(Provide[Container.identity_service])) -> vos.User:
    logger.info("find_user by username")
    return identity_service.find_user_by_username(username)


@router.post("/users")
@inject
def save_user(vo: vos.User,
              identity_service: IdentityService = Depends(Provide[Container.identity_service])) -> ApplicationSuccess:
    logger.info("save user")
    user = models.User()
    user.name = vo.name
    user.realname = vo.realname
    user.email = vo.email
    user.password = vo.password
    user.principal_type = models.PrincipalType(vo.principal_type.value)
    identity_service.save_user(user)
    return ApplicationSuccess.SUCCESS("User added")


# ====================================================================================================
# STAFF
# ====================================================================================================

@router.get("/staffs")
@inject
def find_staffs(page: int = 1, identity_service: IdentityService = Depends(Provide[Container.identity_service])) \
        -> vos.StaffResult:
    logger.info("find_staffs")
    count = identity_service.count_staff()
    staffs = identity_service.find_staffs(((page - 1) * LIMIT), LIMIT)
    return StaffResult(staffs, page, count)


@router.get("/staffs/{identity_no}")
@inject
def find_staff_by_staffname(identity_no: str, identity_service: IdentityService = Depends(
    Provide[Container.identity_service])) -> vos.Staff:
    logger.info("find_staff by identity_no")
    return identity_service.find_staff_by_identity_no(identity_no)


@router.post("/staffs")
@inject
def save_staff(vo: vos.Staff,
               identity_service: IdentityService = Depends(Provide[Container.identity_service])) -> ApplicationSuccess:
    logger.info("save staff")
    staff = models.Staff()
    staff.name = vo.name
    staff.identity_no = vo.identity_no
    staff.department = vo.department
    staff.position = vo.position
    staff.actor_type = models.ActorType(vo.actor_type.value)
    identity_service.save_staff(staff)
    return ApplicationSuccess.SUCCESS("Staff added")


# ====================================================================================================
# CUSTOMER
# ====================================================================================================

@router.get("/customers")
@inject
def find_customers(filter: str, page: int,
                   identity_service: IdentityService = Depends(
                       Provide[Container.identity_service]),
                   current_user: AuthorizedUser = Depends(get_current_user)) -> vos.CustomerResult:
    logger.debug("find_customers")
    count = identity_service.count_customer(filter)
    customers = identity_service.find_customers(filter, ((page - 1) * LIMIT), LIMIT)
    logger.debug(f"customers {customers}")
    logger.debug(f"customers {count}")
    return CustomerResult(customers, page, count)


@router.get("/customers/{identity_no}")
@inject
def find_customer_by_identity_no(identity_no: str,
                                 identity_service: IdentityService = Depends(
                                     Provide[Container.identity_service]),
                                 current_user: AuthorizedUser = Depends(get_current_user)) -> vos.Customer:
    logger.info("find_customer by identity_no")
    return identity_service.find_customer_by_identity_no(identity_no)


@router.post("/customers")
@inject
def save_customer(vo: vos.Customer,
                  identity_service: IdentityService = Depends(Provide[Container.identity_service]),
                  current_user: AuthorizedUser = Depends(get_current_user)
                  ) -> ApplicationSuccess:
    logger.info("save customer")
    customer = models.Customer()
    customer.name = vo.name
    customer.identity_no = vo.identity_no
    customer.address = vo.address
    customer.actor_type = models.ActorType(vo.actor_type.value)
    identity_service.save_customer(customer)
    return ApplicationSuccess.SUCCESS("Customer added")
