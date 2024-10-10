from fastapi import (
    APIRouter,
    Request,
    HTTPException,
    Depends
)
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from server.settings.environments import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    REFRESH_TOKEN_EXPIRE_MINUTES
)
from server.schemas.user import UserAuthData
from server.models.user import User
from werkzeug.security import check_password_hash
import jwt
from datetime import datetime, timedelta
from server.utils import GenerateJWT

user_router = APIRouter(prefix="/user", tags=["Authentication"])


@user_router.post("/auth", summary="JWT Auth")
async def login(user_data: UserAuthData):
    """
    Авторизация пользователя
    """
    user = await User.get(username=user_data.username)
    if not user or not check_password_hash(user.password, user_data.password):
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")

    jwt_service = GenerateJWT()

    return JSONResponse(status_code=200, content=jwt_service.generate_auth_data(username=user.username))
