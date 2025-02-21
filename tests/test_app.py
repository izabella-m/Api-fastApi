from http import HTTPStatus


def test_test_read_root_deve_retornar_ok_e_olamundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá'}


def test_create_users(client):
    response = client.post(
        '/users/',
        json={
            'name': 'teste',
            'email': 'teste@teste.com',
            'age': 12,
            'password': 'teste'
        }
    )

    assert response.status_code == HTTPStatus.CREATED 
    assert response.json() == {
        'name': 'teste',
        'email': 'teste@teste.com',
        'age': 12,
        'id': 1
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {
        'users': [
            {
                'name': 'teste',
                'email': 'teste@teste.com',
                'age': 12,
                'id': 1
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1', 
        json={
            'name': 'teste',
            'email': 'teste@teste.com',
            'age': 12,
            'password': 'teste', 
            'id': 1
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
            'name': 'teste',
            'email': 'teste@teste.com',
            'age': 12,
            'id': 1  
    }
