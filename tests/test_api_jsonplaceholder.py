import requests
import pytest
from utils.logger import logger

@pytest.fixture
def url_base_api():
    return "https://jsonplaceholder.typicode.com/users"


# GET - Obtener usuario
def test_get_user(url_base_api):

    url = f"{url_base_api}/1"
    logger.info(f"GET → {url}")

    response = requests.get(url)
    assert response.status_code == 200, "GET no devolvió 200"

    data = response.json()
    assert "name" in data
    assert data["id"] == 1


# POST - Crear usuario
def test_create_user(url_base_api):

    payload = {
        "name": "Brenda",
        "username": "alumna",
        "email": "brenda@ejemplo.com"
    }

    logger.info(f"POST → {url_base_api} payload={payload}")

    response = requests.post(url_base_api, json=payload)

    assert response.status_code == 201, "POST no devolvió 201"

    data = response.json()
    assert data["name"] == payload["name"]


# DELETE - Eliminar usuario
def test_delete_user(url_base_api):

    url = f"{url_base_api}/1"
    logger.info(f"DELETE → {url}")

    response = requests.delete(url)

    assert response.status_code == 200 or response.status_code == 204

