import logging

from dependency_injector.wiring import Provide
from fastapi.security.utils import get_authorization_scheme_param
from jose import jwt
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from app.conf.containers import Container
from app.conf.jwt import SECRET_KEY, ALGORITHM
from app.identity.business.services import IdentityService

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class CurrentUserMiddleware(BaseHTTPMiddleware):
    identity_service: IdentityService = Provide[Container.identity_service]

    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        logger.info('CurrentUserMiddleware')
        authorization: str = request.headers.get("Authorization")
        scheme, token = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            pass
        else:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            user = self.identity_service.find_user_by_username(username)
            logger.info(user.realname)
            # singleton: SecurityContext = Container.security_context
            # logger.info(singleton.provided.security_context)

        # process the request and get the response
        response = await call_next(request)

        return response
