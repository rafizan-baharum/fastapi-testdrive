from typing import Optional

from pydantic import BaseModel


class AuthorizedUser(BaseModel):
    id: int
    username: str
    email: Optional[str] = None
    realname: Optional[str] = None
    disabled: Optional[bool] = None


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
