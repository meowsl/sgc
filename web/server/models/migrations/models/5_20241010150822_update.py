from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user" (
    "id" TEXT NOT NULL  PRIMARY KEY,
    "username" VARCHAR(128) NOT NULL UNIQUE /* Логин */,
    "password" TEXT NOT NULL  /* Пароль */,
    "firstname" VARCHAR(64)   /* Имя */,
    "lastname" VARCHAR(64)   /* Фамилия */,
    "patronymic" VARCHAR(64)   /* Отчество */,
    "is_active" INT NOT NULL  DEFAULT 1 /* Активен? */
) /* Пользователи */;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "user";"""
