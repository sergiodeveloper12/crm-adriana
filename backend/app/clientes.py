from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from .database import get_db


router = APIRouter()


@router.get("/clientes")
def listar_clientes(
    db: Session = Depends(get_db)
):

    clientes = db.execute(
        text("""
            SELECT 
                id,
                nome,
                email,
                telefone,
                produto,
                mensagem,
                status,
                data_cadastro
            FROM clientes
            ORDER BY id DESC
        """)
    ).fetchall()


    resultado = []

    for cliente in clientes:
        resultado.append({
            "id": cliente.id,
            "nome": cliente.nome,
            "email": cliente.email,
            "telefone": cliente.telefone,
            "produto": cliente.produto,
            "mensagem": cliente.mensagem,
            "status": cliente.status,
            "data_cadastro": cliente.data_cadastro
        })


    return resultado
