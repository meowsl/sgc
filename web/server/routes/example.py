from fastapi import APIRouter
from fastapi.responses import JSONResponse

example_router = APIRouter(prefix="/example", tags=["Example"])


@example_router.get("/test", summary="Get test data")
async def test() -> dict:
    """
    Получение тестовых данных
    """
    return JSONResponse(status_code=200, content={
        "message": "Welcome to FastAPI",
        "data": "This is a test data"
    })
