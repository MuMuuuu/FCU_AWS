from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from jwt import ExpiredSignatureError, PyJWTError
from config import *
from typing import NamedTuple


class LoginState(NamedTuple):
    username: str
    type: str


auth = HTTPBearer()


def parse_token(token: HTTPAuthorizationCredentials = Depends(auth)):
    try:
        payload = jwt.decode(token.credentials, JWT_KEY, algorithms=JWT_ALG)
    except ExpiredSignatureError:
        raise HTTPException(401, "Authentication Expired")
    except PyJWTError:
        raise HTTPException(401, "Invalid Certificate")

    return payload


def get_login_state(payload: dict = Depends(parse_token)):
    return LoginState(username=payload["username"], type=payload["type"])