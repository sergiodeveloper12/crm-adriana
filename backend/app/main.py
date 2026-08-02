from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

from .init_db import criar_tabelas
from .auth import router as auth_router
from .clientes import router as clientes_router


app = FastAPI(
    title="CRM Adriana Froes API",
    version="1.0.0"
)


criar_tabelas()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router, prefix="/api")
app.include_router(clientes_router, prefix="/api")


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

FRONTEND_DIR = os.path.join(
    BASE_DIR,
    "frontend"
)


app.mount(
    "/static",
    StaticFiles(directory=FRONTEND_DIR),
    name="static"
)


@app.get("/")
def home():
    return {
        "status": "CRM Adriana Froes API online"
    }


@app.get("/login.html")
def login():
    return FileResponse(
        os.path.join(FRONTEND_DIR, "login.html")
    )


@app.get("/dashboard.html")
def dashboard():
    return FileResponse(
        os.path.join(FRONTEND_DIR, "dashboard.html")
    )


@app.get("/clientes.html")
def clientes():
    return FileResponse(
        os.path.join(FRONTEND_DIR, "clientes.html")
    )


@app.get("/script.js")
def script():
    return FileResponse(
        os.path.join(FRONTEND_DIR, "script.js")
    )


@app.get("/style.css")
def style():
    return FileResponse(
        os.path.join(FRONTEND_DIR, "style.css")
    )
