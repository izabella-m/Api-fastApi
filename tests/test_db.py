from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from fast_zero.models import User, table_registry


def test_create_user_db():
    engine = create_engine(
        "sqlite:///:memory:"
    )  # criamos a conexão com o banco

    table_registry.metadata.create_all(
        engine
    )  # falamos para o registry pegar os metadados e a partir dele criar a engine com os dados abaixo

    with Session(engine) as session:  # criando uma session a partir dessa engine
        user = User(
            username="Bella",
            email="bella@gmail.com",
            password="secret"
        )

        session.add(user)
        session.commit()  # pega todas as operações e faz a persistência dentro do banco de dados
        result = session.scalar(  # faz um mapeamento e retorna esses objetos python
            select(user).where(User.email == 'bella@gmail.com')
        )

        # return result
        assert result.username == 'Bella'

    assert user.username == "Bella"
