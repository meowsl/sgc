from tortoise import fields
from tortoise.models import Model
from tortoise.signals import pre_save
from werkzeug.security import generate_password_hash
from uuid import uuid4


def get_uuid():
    return uuid4().hex


class User(Model):
    """
    Пользователи
    """
    id = fields.TextField(
        primary_key=True,
        default=get_uuid()
    )
    username = fields.CharField(
        max_length=128,
        unique=True,
        description="Логин"
    )
    password = fields.TextField(
        description="Пароль"
    )
    firstname = fields.CharField(
        max_length=64,
        null=True,
        description="Имя"
    )
    lastname = fields.CharField(
        max_length=64,
        null=True,
        description="Фамилия"
    )
    patronymic = fields.CharField(
        max_length=64,
        null=True,
        description="Отчество"
    )
    is_active = fields.BooleanField(
        default=True,
        description="Активен?"
    )

    def get_fullname(self):
        if self.patronymic:
            return f"{self.lastname} {self.firstname} {self.patronymic}"
        else:
            return f"{self.lastname} {self.firstname}"

    def get_shortname(self):
        if self.patronymic:
            return f"{self.lastname} {self.firstname[0]}. {self.patronymic[0]}."
        else:
            return f"{self.lastname} {self.firstname[0]}."


@pre_save(User)
async def pre_save_user(sender, instance, using_db, update_fields):
    """
    Предварительное хэширование пароля
    """
    if instance.password:
        instance.password = generate_password_hash(instance.password)
