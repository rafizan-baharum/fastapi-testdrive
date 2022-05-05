import logging
from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

crypt_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password, hashed_password):
    # return crypt_context.verify(plain_password, hashed_password)
    return plain_password == hashed_password