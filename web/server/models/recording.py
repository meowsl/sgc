from tortoise import fields
from tortoise.models import Model
from server.schemas import RecordingScheme


class Recording(Model):
    """
    Полученные измерения
    """
    id = fields.IntField(
        pk=True
    )
    date = fields.DateField(
        auto_now=True,
        description="Дата измерения"
    )
    time = fields.TimeField(
        description="Время измерения"
    )
    lower_frequency = fields.BigIntField(
        description="Нижняя частота (Гц)"
    )
    upper_frequency = fields.BigIntField(
        description="Верхняя частота (Гц)"
    )
    bin_width = fields.FloatField(
        description="Ширина бина (Гц)"
    )
    count_selection = fields.IntField(
        description="Кол-во выборок"
    )

    class Meta:
        table = "Сигналы"
        schema = RecordingScheme
