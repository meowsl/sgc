from pydantic import BaseModel


class UserAuthData(BaseModel):
    """
    Схема данных авторизации
    """
    username: str
    password: str
