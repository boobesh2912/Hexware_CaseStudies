"""
Tests for User endpoints
POST /users/
GET  /users/
GET  /users/{id}
PUT  /users/{id}
DELETE /users/{id}
"""

def test_create_user(client):
    response = client.post("/users/", json={
        "name": "Arun Kumar",
        "email": "arun@example.com",
        "role": "customer",
        "password": "secret123"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Arun Kumar"
    assert data["email"] == "arun@example.com"
    assert data["role"] == "customer"
    assert "id" in data
    # password must NEVER be returned
    assert "password" not in data
    assert "hashed_password" not in data


def test_create_loan_officer(client):
    response = client.post("/users/", json={
        "name": "Priya Officer",
        "email": "priya@example.com",
        "role": "loan_officer",
        "password": "officer123"
    })
    assert response.status_code == 201
    assert response.json()["role"] == "loan_officer"


def test_create_duplicate_user(client):
    # Create first time
    client.post("/users/", json={
        "name": "Duplicate User",
        "email": "dup@example.com",
        "role": "customer",
        "password": "pass123"
    })
    # Create again with same email
    response = client.post("/users/", json={
        "name": "Duplicate User 2",
        "email": "dup@example.com",
        "role": "customer",
        "password": "pass456"
    })
    assert response.status_code == 400
    assert "already exists" in response.json()["detail"]


def test_get_all_users(client):
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_user_by_id(client):
    # Create a user first
    create = client.post("/users/", json={
        "name": "Get Test",
        "email": "gettest@example.com",
        "role": "customer",
        "password": "pass123"
    })
    user_id = create.json()["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id


def test_get_user_not_found(client):
    response = client.get("/users/99999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]


def test_update_user(client):
    create = client.post("/users/", json={
        "name": "Before Update",
        "email": "update@example.com",
        "role": "customer",
        "password": "pass123"
    })
    user_id = create.json()["id"]

    response = client.put(f"/users/{user_id}", json={
        "name": "After Update",
        "email": "update@example.com",
        "role": "customer",
        "password": "pass123"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "After Update"


def test_delete_user(client):
    create = client.post("/users/", json={
        "name": "Delete Me",
        "email": "deleteme@example.com",
        "role": "customer",
        "password": "pass123"
    })
    user_id = create.json()["id"]

    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 204

    # Verify it's gone
    get = client.get(f"/users/{user_id}")
    assert get.status_code == 404


def test_pagination(client):
    response = client.get("/users/?skip=0&limit=2")
    assert response.status_code == 200
    assert len(response.json()) <= 2