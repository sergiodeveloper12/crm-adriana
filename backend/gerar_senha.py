from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

senha = "Adriana@2026"

hash_senha = pwd_context.hash(senha)

print(hash_senha)
