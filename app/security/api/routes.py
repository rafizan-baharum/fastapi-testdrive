import logging
from datetime import timedelta

from dependency_injector.wiring import Provide, inject
from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt, JWTError
from starlette import status

from app.conf.containers import Container
from app.conf.jwt import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, verify_password, SECRET_KEY, \
    ALGORITHM
from app.identity.business.services import IdentityService
from app.identity.domain.models import User
from app.security.api.vos import AuthorizedUser, Token, TokenData

logger = logging.getLogger(__name__)

router = APIRouter(tags=["Security"])

@router.post("/token", response_model=Token)
@inject
def login(form_data: OAuth2PasswordRequestForm = Depends(),
          identity_service: IdentityService = Depends(Provide[Container.identity_service])):
    username = form_data.username
    password = form_data.password

    logging.info(username)
    logging.info(password)


# authenticate
    authenticated: bool = False
    try:
        user = identity_service.find_user_by_username(username)
        authenticated = verify_password(password, user.password)
    except User.DoesNotExist:
        authenticated = False

    if authenticated:
        access_token = create_access_token(
            data={"sub": username}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")


@inject
def get_current_user(token: str = Depends(Container.oauth2_scheme),
                     identity_service: IdentityService = Depends(Provide[Container.identity_service])):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    logging.info(token)

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    # find user
    user = identity_service.find_user_by_username(token_data.username)
    if user is None:
        raise credentials_exception
    return user

@router.get("/users/me")
@inject
def get_current_user(current_user: AuthorizedUser = Depends(get_current_user)):
    logging.info("get_current_user")
    return current_user
