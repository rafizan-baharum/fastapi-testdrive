import logging
from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.conf.containers import Container
from app.core.api.vos import ApplicationSuccess
from app.system.api import vos
from app.system.business.services import SystemService
from app.system.domain import models

logger = logging.getLogger("routes")

router = APIRouter(tags=["System"])

# ====================================================================================================
# EMAIL TEMPLATE
# ====================================================================================================

@router.get("/email-templates")
@inject
def find_email_templates(system_service: SystemService = Depends(Provide[Container.system_service])) -> List[
    vos.EmailTemplate]:
    logger.info("find_email_templates")
    return system_service.find_email_templates()


@router.get("/email-templates/{code}")
@inject
def find_email_template_by_email_code(code: str,
                                      system_service: SystemService = Depends(
                                          Provide[Container.system_service])) -> vos.EmailTemplate:
    logger.info("find_email_template by code")
    return system_service.find_email_template_by_code(code)


@router.post("/email-templates")
@inject
def save_email_template(vo: vos.EmailTemplate,
                        system_service: SystemService = Depends(
                            Provide[Container.system_service])) -> ApplicationSuccess:
    logger.info("save_email_template")
    template = models.EmailTemplate()
    template.code = vo.code
    template.description = vo.description
    template.subject = vo.subject
    template.template = vo.template
    system_service.save_email_template(template)
    return ApplicationSuccess.SUCCESS("Email template added")


# ====================================================================================================
# EMAIL QUEUE
# ====================================================================================================

@router.get("/email-queues")
@inject
def find_email_queues(system_service: SystemService = Depends(Provide[Container.system_service])) -> List[
    vos.EmailTemplate]:
    logger.info("find_email_queues")
    return system_service.find_email_queues()


@router.get("/email-queues/{code}")
@inject
def find_email_queue_by_code(code: str,
                             system_service: SystemService = Depends(
                                 Provide[Container.system_service])) -> vos.EmailTemplate:
    logger.info("find_email_queue by code")
    return system_service.find_email_queue_by_code(code)


@router.post("/email-queues")
@inject
def save_email_queue(vo: vos.EmailTemplate,
                     system_service: SystemService = Depends(
                         Provide[Container.system_service])) -> ApplicationSuccess:
    logger.info("save_email_queue")
    template = models.EmailTemplate()
    template.code = vo.code
    template.description = vo.description
    template.subject = vo.subject
    template.template = vo.template
    system_service.save_email_queue(template)
    return ApplicationSuccess.SUCCESS("Email template added")


# ====================================================================================================
# EMAIL QUEUE
# ====================================================================================================

@router.get("/sequence-generators")
@inject
def find_sequence_generators(system_service: SystemService = Depends(Provide[Container.system_service])) -> List[
    vos.SequenceGenerator]:
    logger.info("find_sequence_generators")
    return system_service.find_sequence_generators()


@router.get("/sequence-generators/{code}")
@inject
def find_sequence_generator_by_code(code: str,
                                    system_service: SystemService = Depends(
                                        Provide[Container.system_service])) -> vos.SequenceGenerator:
    logger.info("find_sequence_generator by code")
    return system_service.find_sequence_generator_by_code(code)


@router.post("/sequence-generators")
@inject
def save_sequence_generator(vo: vos.SequenceGenerator,
                            system_service: SystemService = Depends(
                                Provide[Container.system_service])) -> ApplicationSuccess:
    logger.info("save_sequence_generator")
    generator = models.SequenceGenerator()
    generator.code = vo.code
    generator.description = vo.description
    generator.reference_format = vo.reference_format
    generator.sequence_format = vo.sequence_format
    generator.current_value = vo.current_value
    generator.increment_value = vo.increment_value
    system_service.save_sequence_generator(generator)
    return ApplicationSuccess.SUCCESS("Sequence generator added")
