from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.routes import user_router
from server.settings.database import init_db

app = FastAPI(
    root_path="/api/v1",
    docs_url="/docs",
    openapi_url="/openapi.json"
)
init_db(app=app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=[
        "Content-Type",
        "Authorization",
        "Access-Control-Allow-Origin",
        "Access-Control-Allow-Credentials"
    ]
)

app.include_router(user_router)
