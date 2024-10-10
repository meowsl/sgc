from tortoise import fields
from tortoise.models import Model
from server.schemas import ExampleScheme


class Example(Model):
    """
    Пример базы
    """

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()

    class Meta:
        table = "Пример"
        schema = ExampleScheme
