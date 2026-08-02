from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from .init_db import criar_tabelas
from .auth import router as auth_router
from .clientes import router as clientes_router


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


app.include_router(
    auth_router,
    prefix="/api"
)

app.include_router(
    clientes_router,
    prefix="/api"
)


# Servir frontend
app.mount(
    "/static",
    StaticFiles(directory="../frontend"),
    name="static"
)


@app.get("/")
def home():
    return FileResponse("../frontend/login.html")


@app.get("/login.html")
def login():
    return FileResponse("../frontend/login.html")


@app.get("/dashboard.html")
def dashboard():
    return FileResponse("../frontend/dashboard.html")


@app.get("/clientes.html")
def clientes():
    return FileResponse("../frontend/clientes.html")
