import pytest

from users.models import User


@pytest.fixture
def create_user_request(client):
    return client.post(
        "/users/", {"username": "test", "email": "test@user.com", "password": "test"}
    )


@pytest.mark.django_db
def test_should_return_all_users(client, create_user_request):
    response = client.get("/users/")
    assert response.status_code == 200
    assert User.objects.first().username == "test"


@pytest.mark.django_db
def test_should_create_user(client, create_user_request):
    assert create_user_request.status_code == 201
    assert ("username", "test") in create_user_request.data.items()


@pytest.mark.django_db
def test_should_return_user_by_id(client, create_user_request):
    user = create_user_request.data
    response = client.get(f"/users/{user['id']}/")
    assert response.status_code == 403

    client.login(username="test", password="test")
    response = client.get(f"/users/{user['id']}/")
    assert response.status_code == 200
    assert ("username", "test") in response.data.items()


@pytest.mark.django_db
def test_should_delete_user(client, create_user_request):
    user = create_user_request.data
    response = client.delete(f"/users/{user['id']}/")
    assert response.status_code == 403

    client.login(username="test", password="test")
    response = client.delete(f"/users/{user['id']}/")
    assert response.status_code == 204

    assert User.objects.filter(id=user["id"]).exists() == False
