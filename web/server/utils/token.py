from datetime import datetime, timedelta
from server.settings.environments import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    REFRESH_TOKEN_EXPIRE_MINUTES
)
import jwt


class GenerateJWT():
    """
    Генерация JWT данных
    """

    def _create_access_token(self, data: dict, expires_delta: timedelta):
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def _create_refresh_token(self, data: dict, expires_delta: timedelta):
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def generate_auth_data(self, username):
        """
        """
        return {
            "access": self._create_access_token(
                data={"sub": username},
                expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            ),
            "refresh": self._create_refresh_token(
                data={"sub": username},
                expires_delta=timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
            ),
            "token_type": "Bearer"
        }
