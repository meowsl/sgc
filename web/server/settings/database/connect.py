from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise
from server.settings.environments import (
    USE_SQLITE,
    DATABASE_URL
)
from server.settings.base import DEV_DATABASE_FILE

Tortoise.init_models(["server.models"], "models")

if USE_SQLITE:
    TORTOISE_ORM = {
        "connections": {
            "default": f"sqlite://{DEV_DATABASE_FILE}"
        },
        "apps": {
            "models": {
                "models": ["server.models", "aerich.models"],
                "default_connection": "default"
            }
        }
    }
else:
    TORTOISE_ORM = {
        "connections": {
            "default": DATABASE_URL
        },
        "apps": {
            "models": {
                "models": ["server.models", "aerich.models"],
                "default_connection": "default"
            }
        }
    }


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app=app,
        config=TORTOISE_ORM,
        modules={
            "models": ["server.models", "aerich.models"]
        },
        generate_schemas=True,
        add_exception_handlers=True
    )
