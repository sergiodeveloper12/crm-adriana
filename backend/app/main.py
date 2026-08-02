from sqlalchemy import text
from .database import engine
from passlib.context import CryptContext


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def criar_tabelas():

    with engine.connect() as conn:

        # CLIENTES
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS clientes (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(150),
                telefone VARCHAR(30),
                produto VARCHAR(100),
                mensagem TEXT,
                status VARCHAR(50) DEFAULT 'Novo',
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """))


        # USUARIOS
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id SERIAL PRIMARY KEY,
                usuario VARCHAR(50) UNIQUE NOT NULL,
                senha_hash VARCHAR(255) NOT NULL,
                perfil VARCHAR(50) DEFAULT 'admin'
            );
        """))


        usuarios = [
            {
                "usuario": "admin",
                "senha": "123456",
                "perfil": "admin"
            },
            {
                "usuario": "adriana",
                "senha": "Adriana@2026",
                "perfil": "admin"
            }
        ]


        for user in usuarios:

            existe = conn.execute(
                text("""
                    SELECT id
                    FROM usuarios
                    WHERE usuario = :usuario
                """),
                {
                    "usuario": user["usuario"]
                }
            ).fetchone()


            if not existe:

                senha_hash = pwd_context.hash(
                    user["senha"]
                )

                conn.execute(
                    text("""
                        INSERT INTO usuarios
                        (
                            usuario,
                            senha_hash,
                            perfil
                        )
                        VALUES
                        (
                            :usuario,
                            :senha_hash,
                            :perfil
                        )
                    """),
                    {
                        "usuario": user["usuario"],
                        "senha_hash": senha_hash,
                        "perfil": user["perfil"]
                    }
                )


        conn.commit()


if __name__ == "__main__":
    criar_tabelas()
