from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

# Существующие пользователи
users = [
    {
        'id': 1,
        'name': 'Ivan Ivanov',
        'email': 'i.i.ivanov@mail.com',
    },
    {
        'id': 2,
        'name': 'Petr Petrov',
        'email': 'p.p.petrov@mail.com',
    }
]

def test_get_existed_user():
    '''Получение существующего пользователя'''
    response = client.get("/api/v1/user", params={'email': users[0]['email']})
    assert response.status_code == 200
    assert response.json() == users[0]

def test_get_unexisted_user():
    '''Получение несуществующего пользователя'''
    response = client.get("/api/v1/user", params={"email": "missing@example.com"})
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

def test_create_user_with_valid_email():
    '''Создание пользователя с уникальной почтой'''
    data = {"name": "Maxim Konovalov", "email": "mkonovalov@example.com"}
    response = client.post("/api/v1/user", json=data)
    assert response.status_code == 201
    assert isinstance(response.json(), int)
    result = client.get("/api/v1/user", params={"email": data["email"]})
    assert result.status_code == 200
    assert result.json() == {"id": response.json(), **data}

def test_create_user_with_invalid_email():
    '''Создание пользователя с почтой, которую использует другой пользователь'''
    response = client.post("/api/v1/user", json={"name": "Other", "email": users[0]["email"]})
    assert response.status_code == 409
    assert response.json() == {"detail": "User with this email already exists"}
    original = client.get("/api/v1/user", params={"email": users[0]["email"]})
    assert original.json() == users[0]

def test_delete_user():
    '''Удаление пользователя'''
    response = client.delete("/api/v1/user", params={"email": users[0]["email"]})
    assert response.status_code == 204
    assert response.content == b""
    result = client.get("/api/v1/user", params={"email": users[0]["email"]})
    assert result.status_code == 404
    other = client.get("/api/v1/user", params={"email": users[1]["email"]})
    assert other.json() == users[1]