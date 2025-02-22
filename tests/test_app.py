from http import HTTPStatus


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

# def test_read_users_for_id(client):
#         response = client.get('/users/1', json={
#         'name': 'teste',
#         'email': 'teste@teste.com',
#         'age': 12,
#         'password': 'teste'
#     })

#     # Buscando o usuário pelo ID 1
#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {
#         'id': 1,
#         'name': 'teste',
#         'email': 'teste@teste.com',
#         # 'age': 12
#     }

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

def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.json() ==  {'message': 'user deleted'}