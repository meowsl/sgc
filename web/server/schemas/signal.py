from pydantic import BaseModel


class SignalScheme(BaseModel):
    """
    Схема сигнала
    """
    id: int
    strength: float

    class Config:
        from_attributes = True
