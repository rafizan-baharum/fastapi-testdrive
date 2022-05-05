import logging
from logging.config import dictConfig

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi_events.handlers.local import local_handler
from fastapi_events.middleware import EventHandlerASGIMiddleware
from fastapi_route_log.log_request import LoggingRoute

from app.booking.api import routes as booking_routes
from app.common.api import routes as common_routes
from app.conf.logging import LogConfig
from app.conf.middlewares import CurrentUserMiddleware
from app.identity.api import routes as identity_routes
from app.security.api import routes as security_routes
from app.system.api import routes as system_routes

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def my_schema():
    openapi_schema = get_openapi(
        title="Rebana Application API",
        version="1.0",
        routes=app.routes,
    )
    openapi_schema["info"] = {
        "title" : "Rebana Application API",
        "version" : "1.0",
        "description" : "Rebana Application API",
        "termsOfService": "http://rebana.io",
        "contact": {
            "name": "Get Help with this API",
            "url": "http://rebana.io",
            "email": "support@rebana.io"
        },
        "license": {
            "name": "MIT 2.0",
            "url": "https://www.mit.org/licenses/LICENSE-2.0.html"
        },
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def create_app() -> FastAPI:

    dictConfig(LogConfig().dict())
    logger = logging.getLogger("root")

    from app.conf import containers
    container = containers.Container()

    db = container.db()
    db.create_database()

    app = FastAPI(title="Rebana Test API")
    app.openapi = my_schema
    app.container = container
    app.router.route_class = LoggingRoute

    app.include_router(identity_routes.router, prefix='/api/identity')
    app.include_router(booking_routes.router, prefix='/api/booking')
    app.include_router(common_routes.router, prefix='/api/common')
    app.include_router(system_routes.router, prefix='/api/system')
    app.include_router(security_routes.router, prefix='/api/security')
    try:
        app.add_middleware(CurrentUserMiddleware)
        app.add_middleware(EventHandlerASGIMiddleware, handlers=[local_handler])
    except Exception as e:
        logger.info(e.__cause__)
        pass

    return app


app = create_app()
