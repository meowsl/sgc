from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "example" RENAME TO "Пример";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "Пример" RENAME TO "example";"""
