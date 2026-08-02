from sqlalchemy import text
from .database import engine


def criar_tabelas():

    with engine.connect() as conn:
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

        conn.commit()


if __name__ == "__main__":
    criar_tabelas()
