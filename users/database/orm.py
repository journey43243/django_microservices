from .core import engine_pg,session_var
from models import Base, Users
from .security.users_password import get_password_hash


def create_tables() -> None:
    Base.metadata.create_all(engine_pg)

def drop_tables() -> None:
    Base.metadata.drop_all(engine_pg)


async def create_user(username : str, password : str, email : str) -> None:

    hash_psw = get_password_hash(password)
    user = Users(email = email, password = hash_psw, username = username)

    with session_var() as session:
        session.add(user)
        session.commit()

    return username







