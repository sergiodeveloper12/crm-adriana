from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from pathlib import Path

from .init_db import criar_tabelas
from .auth import router as auth_router
from .clientes import router as clientes_router


# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"


# Criar tabelas no banco
criar_tabelas()


app = FastAPI(
    title="CRM Adriana Froes API",
    version="1.0.0"
)


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


# Arquivos do frontend
app.mount(
    "/static",
    StaticFiles(directory=FRONTEND_DIR),
    name="static"
)


@app.get("/")
def home():
    return FileResponse(
        FRONTEND_DIR / "login.html"
    )


@app.get("/login.html")
def login():
    return FileResponse(
        FRONTEND_DIR / "login.html"
    )


@app.get("/dashboard.html")
def dashboard():
    return FileResponse(
        FRONTEND_DIR / "dashboard.html"
    )


@app.get("/clientes.html")
def clientes():
    return FileResponse(
        FRONTEND_DIR / "clientes.html"
    )
