from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .init_db import criar_tabelas
from .auth import router as auth_router
from .clientes import router as clientes_router


app = FastAPI(
    title="CRM Adriana Froes API",
    version="1.0.0"
)

criar_tabelas()
