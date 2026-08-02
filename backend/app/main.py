from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .init_db import criar_tabelas
from .auth import router as auth_router
from .clientes import router as clientes_router


app = FastAPI(
    title="CRM Adriana Froes API",
    version="1.0.0"
)


# cria tabelas e usuários ao iniciar
criar_tabelas()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    auth_router,
    prefix="/api"
)


app.include_router(
    clientes_router,
    prefix="/api"
)


@app.get("/")
def home():
    return {
        "status": "CRM Adriana Froes API online"
    }
