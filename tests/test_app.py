from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_test_read_root_deve_retornar_ok_e_olamundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundooo'}
