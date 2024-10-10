from tortoise import fields
from tortoise.models import Model
from server.schemas import SignalScheme


class Signal(Model):
    """
    Сигналы
    """

    id = fields.IntField(
        pk=True
    )
    recording = fields.ForeignKeyField(
        "models.Recording",
        related_name="signals",
    )

    strength = fields.FloatField(
        description="Уровень сигнала (дБ)"
    )

    class Meta:
        table = "Сигнал"
        schema = SignalScheme
