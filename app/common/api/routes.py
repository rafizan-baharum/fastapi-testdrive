import logging
from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.conf.containers import Container
from app.core.api.vos import ApplicationSuccess
from app.common.api import vos
from app.common.business.services import CommonService
from app.common.domain import models
from app.core.constants import LIMIT
from app.security.api.routes import get_current_user
from app.security.api.vos import AuthorizedUser

logger = logging.getLogger("routes")

router = APIRouter(tags=["Common"])


# ====================================================================================================
# DISTRICT CODE
# ====================================================================================================

@router.get("/district-codes")
@inject
def find_district_codes(filter: str, page: int,
                        common_service: CommonService = Depends(Provide[Container.common_service])) -> List[
    vos.DistrictCode]:
    logger.info("find_district_codes")
    return common_service.find_district_codes(filter, (page - 1) * LIMIT, LIMIT)


@router.get("/district-codes/{code}")
@inject
def find_district_code_by_district_codename(code: str,
                                            common_service: CommonService = Depends(
                                                Provide[Container.common_service])) -> vos.DistrictCode:
    logger.info("find_district_code by username")
    return common_service.find_district_code_by_code(code)


@router.post("/district-codes")
@inject
def save_district_code(vo: vos.DistrictCode,
                       common_service: CommonService = Depends(
                           Provide[Container.common_service])) -> ApplicationSuccess:
    logger.info("save user")
    districtCode = models.DistrictCode()
    districtCode.code = vo.code
    districtCode.description = vo.description
    common_service.save_district_code(districtCode)
    return ApplicationSuccess.SUCCESS("District code added")


# ====================================================================================================
# STATE CODE
# ====================================================================================================

@router.get("/state-codes")
@inject
def find_state_codes(filter: str, page: int,
                     common_service: CommonService = Depends(Provide[Container.common_service]),
                     current_user: AuthorizedUser = Depends(get_current_user)
                     ) -> List[
    vos.StateCode]:
    logger.info("find_state_codes")
    return common_service.find_state_codes(filter, (page - 1) * LIMIT, LIMIT)


@router.get("/state-codes/{code}")
@inject
def find_state_code_by_state_codename(code: str,
                                      common_service: CommonService = Depends(
                                          Provide[Container.common_service])) -> vos.StateCode:
    logger.info("find_state_code by username")
    return common_service.find_state_code_by_code(code)


@router.post("/state-codes")
@inject
def save_state_code(vo: vos.StateCode,
                    common_service: CommonService = Depends(
                        Provide[Container.common_service])) -> ApplicationSuccess:
    logger.info("save state code")
    state_code = models.StateCode()
    state_code.code = vo.code
    state_code.description = vo.description
    common_service.save_state_code(state_code)
    return ApplicationSuccess.SUCCESS("State code added")
