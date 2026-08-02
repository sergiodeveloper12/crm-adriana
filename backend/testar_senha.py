from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

senha_digitada = "Adriana@2026"

hash_banco = "$2b$12$QA9.8E1FNUb5/ueRItfPA.hpCUCqKxVs2UcpNb4PbYmUh6ah9JkYO"

resultado = pwd_context.verify(
    senha_digitada,
    hash_banco
)

print(resultado)
