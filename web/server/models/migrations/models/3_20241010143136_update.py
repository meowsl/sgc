from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "Сигналы" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "date" DATE NOT NULL  /* Дата измерения */,
    "time" TIME NOT NULL  /* Время измерения */,
    "lower_frequency" BIGINT NOT NULL  /* Нижняя частота (Гц) */,
    "upper_frequency" BIGINT NOT NULL  /* Верхняя частота (Гц) */,
    "bin_width" REAL NOT NULL  /* Ширина бина (Гц) */,
    "count_selection" INT NOT NULL  /* Кол-во выборок */
) /* Полученные измерения */;
        CREATE TABLE IF NOT EXISTS "Сигнал" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "strength" REAL NOT NULL  /* Уровень сигнала (дБ) */,
    "recording_id" INT NOT NULL REFERENCES "Сигналы" ("id") ON DELETE CASCADE
) /* Сигналы */;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "Сигналы";
        DROP TABLE IF EXISTS "Сигнал";"""
