from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .init_db import criar_tabelas
from .auth import router as auth_router
from .clientes import router as clientes_router


app = FastAPI(
    title="CRM Adriana Froes API",
    version="1.0.0"
)


# cria tabelas automaticamente no PostgreSQL
criar_tabelas()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Rotas da API
app.include_router(
    auth_router,
    prefix="/api"
)


app.include_router(
    clientes_router,
    prefix="/api"
)


# Caminho da pasta frontend
BASE_DIR = Path(__file__).resolve().parent.parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"


# Publica HTML, JS e CSS
app.mount(
    "/",
    StaticFiles(
        directory=FRONTEND_DIR,
        html=True
    ),
    name="frontend"
)
