from sqlalchemy import text
from .database import engine
from passlib.context import CryptContext


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def criar_tabelas():

    with engine.connect() as conn:

        # tabela clientes
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


        # tabela usuarios
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id SERIAL PRIMARY KEY,
                usuario VARCHAR(50) UNIQUE NOT NULL,
                senha_hash VARCHAR(255) NOT NULL,
                perfil VARCHAR(50) DEFAULT 'admin'
            );
        """))


        # cria usuário admin se não existir
        usuario_existente = conn.execute(
            text("""
                SELECT id
                FROM usuarios
                WHERE usuario='admin'
            """)
        ).fetchone()


        if not usuario_existente:

            senha = pwd_context.hash("123456")

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
                        'admin',
                        :senha,
                        'admin'
                    )
                """),
                {
                    "senha": senha
                }
            )


        conn.commit()


if __name__ == "__main__":
    criar_tabelas()
