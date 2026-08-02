from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import text

from .database import get_db


router = APIRouter()

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


class LoginRequest(BaseModel):
    usuario: str
    senha: str


@router.post("/login")
def login(
    dados: LoginRequest,
    db: Session = Depends(get_db)
):

    usuario = db.execute(
        text(
            "SELECT * FROM usuarios WHERE usuario=:usuario"
        ),
        {
            "usuario": dados.usuario
        }
    ).fetchone()


    if not usuario:
        raise HTTPException(
            status_code=401,
            detail="Usuário inválido"
        )


    senha_valida = pwd_context.verify(
        dados.senha,
        usuario.senha_hash
    )


    if not senha_valida:
        raise HTTPException(
            status_code=401,
            detail="Senha inválida"
        )


    return {
        "mensagem": "Login realizado com sucesso",
        "usuario": usuario.usuario,
        "perfil": usuario.perfil
    }
