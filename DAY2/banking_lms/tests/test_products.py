"""
Tests for Loan Product endpoints
POST   /loan-products/
GET    /loan-products/
GET    /loan-products/{id}
PUT    /loan-products/{id}
DELETE /loan-products/{id}
"""

def test_create_loan_product(client):
    response = client.post("/loan-products/", json={
        "product_name": "Home Loan",
        "interest_rate": 8.5,
        "max_amount": 5000000.0,
        "tenure_months": 240,
        "description": "For purchasing home"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["product_name"] == "Home Loan"
    assert data["interest_rate"] == 8.5
    assert data["max_amount"] == 5000000.0
    assert "id" in data


def test_create_product_invalid_interest(client):
    # interest_rate must be > 0
    response = client.post("/loan-products/", json={
        "product_name": "Bad Loan",
        "interest_rate": -1.0,
        "max_amount": 100000.0,
        "tenure_months": 12
    })
    assert response.status_code == 422


def test_create_product_invalid_amount(client):
    # max_amount must be > 0
    response = client.post("/loan-products/", json={
        "product_name": "Bad Loan 2",
        "interest_rate": 5.0,
        "max_amount": 0,
        "tenure_months": 12
    })
    assert response.status_code == 422


def test_get_all_products(client):
    response = client.get("/loan-products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_product_by_id(client):
    create = client.post("/loan-products/", json={
        "product_name": "Personal Loan",
        "interest_rate": 12.0,
        "max_amount": 500000.0,
        "tenure_months": 60
    })
    product_id = create.json()["id"]

    response = client.get(f"/loan-products/{product_id}")
    assert response.status_code == 200
    assert response.json()["id"] == product_id


def test_get_product_not_found(client):
    response = client.get("/loan-products/99999")
    assert response.status_code == 404


def test_update_product(client):
    create = client.post("/loan-products/", json={
        "product_name": "Car Loan",
        "interest_rate": 10.0,
        "max_amount": 1000000.0,
        "tenure_months": 84
    })
    product_id = create.json()["id"]

    response = client.put(f"/loan-products/{product_id}", json={
        "interest_rate": 9.5
    })
    assert response.status_code == 200
    assert response.json()["interest_rate"] == 9.5


def test_delete_product(client):
    create = client.post("/loan-products/", json={
        "product_name": "Delete Product",
        "interest_rate": 7.0,
        "max_amount": 200000.0,
        "tenure_months": 24
    })
    product_id = create.json()["id"]

    response = client.delete(f"/loan-products/{product_id}")
    assert response.status_code == 204

    get = client.get(f"/loan-products/{product_id}")
    assert get.status_code == 404


def test_pagination(client):
    response = client.get("/loan-products/?skip=0&limit=2")
    assert response.status_code == 200
    assert len(response.json()) <= 2