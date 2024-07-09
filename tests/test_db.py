from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='souza',
        email='souza@teste.com',
        password='Mminh@Nov@Senha123',
    )

    session.add(user)
    session.commit()

    session.scalar(select(User).where(User.email == 'souza@teste.com'))

    assert user.username == 'souza'
