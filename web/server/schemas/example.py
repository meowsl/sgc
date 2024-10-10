from pydantic import BaseModel


class ExampleScheme(BaseModel):
    """
    Схема примера
    """
    id: int
    name: str
    description: str
