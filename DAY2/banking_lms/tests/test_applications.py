"""
Tests for Loan Application endpoints
POST /loan-applications/
GET  /loan-applications/
GET  /loan-applications/{id}
PUT  /loan-applications/{id}/status

Also tests all business rules from PDF:
- requested_amount > max_amount blocked
- only loan_officer can approve
- cannot disburse unless approved
"""

import pytest

# Helper functions to create test data
def create_customer(client, email="customer@test.com"):
    res = client.post("/users/", json={
        "name": "Test Customer",
        "email": email,
        "role": "customer",
        "password": "pass123"
    })
    return res.json()["id"]


def create_officer(client, email="officer@test.com"):
    res = client.post("/users/", json={
        "name": "Test Officer",
        "email": email,
        "role": "loan_officer",
        "password": "pass123"
    })
    return res.json()["id"]


def create_product(client, max_amount=500000.0, name="Test Product"):
    res = client.post("/loan-products/", json={
        "product_name": name,
        "interest_rate": 10.0,
        "max_amount": max_amount,
        "tenure_months": 60
    })
    return res.json()["id"]


# ── Basic Tests ──────────────────────────────────────────────

def test_create_application(client):
    customer_id = create_customer(client, "app1@test.com")
    product_id = create_product(client, name="App Product 1")

    response = client.post("/loan-applications/", json={
        "user_id": customer_id,
        "product_id": product_id,
        "requested_amount": 100000.0
    })
    assert response.status_code == 201
    data = response.json()
    assert data["user_id"] == customer_id
    assert data["product_id"] == product_id
    assert data["status"] == "pending"  # always starts as pending


def test_get_all_applications(client):
    response = client.get("/loan-applications/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_application_by_id(client):
    customer_id = create_customer(client, "app2@test.com")
    product_id = create_product(client, name="App Product 2")

    create = client.post("/loan-applications/", json={
        "user_id": customer_id,
        "product_id": product_id,
        "requested_amount": 50000.0
    })
    app_id = create.json()["id"]

    response = client.get(f"/loan-applications/{app_id}")
    assert response.status_code == 200
    assert response.json()["id"] == app_id


def test_get_application_not_found(client):
    response = client.get("/loan-applications/99999")
    assert response.status_code == 404


# ── Business Rule Tests ──────────────────────────────────────

def test_amount_exceeds_max_blocked(client):
    """PDF Rule: requested_amount cannot exceed product max_amount"""
    customer_id = create_customer(client, "exceed@test.com")
    product_id = create_product(client, max_amount=100000.0, name="Low Max Product")

    response = client.post("/loan-applications/", json={
        "user_id": customer_id,
        "product_id": product_id,
        "requested_amount": 999999.0  # way more than max
    })
    assert response.status_code == 400
    assert "exceeds" in response.json()["detail"]


def test_invalid_user_blocked(client):
    """Cannot apply with non-existent user"""
    product_id = create_product(client, name="Valid Product X")
    response = client.post("/loan-applications/", json={
        "user_id": 99999,
        "product_id": product_id,
        "requested_amount": 50000.0
    })
    assert response.status_code == 404


def test_invalid_product_blocked(client):
    """Cannot apply with non-existent product"""
    customer_id = create_customer(client, "invprod@test.com")
    response = client.post("/loan-applications/", json={
        "user_id": customer_id,
        "product_id": 99999,
        "requested_amount": 50000.0
    })
    assert response.status_code == 404


def test_only_loan_officer_can_approve(client):
    """PDF Rule: only loan_officer can approve/reject"""
    # Create a customer (NOT an officer)
    customer_id = create_customer(client, "nonofficer@test.com")
    product_id = create_product(client, name="Officer Test Product")

    create = client.post("/loan-applications/", json={
        "user_id": customer_id,
        "product_id": product_id,
        "requested_amount": 50000.0
    })
    app_id = create.json()["id"]

    # Try to approve using customer (not a loan_officer)
    response = client.put(f"/loan-applications/{app_id}/status", json={
        "status": "approved",
        "approved_amount": 50000.0,
        "processed_by": customer_id  # customer trying to approve
    })
    assert response.status_code == 403
    assert "loan officer" in response.json()["detail"].lower()


def test_approve_application(client):
    """Loan officer can approve successfully"""
    customer_id = create_customer(client, "approve@test.com")
    officer_id = create_officer(client, "approveofficer@test.com")
    product_id = create_product(client, name="Approve Product")

    create = client.post("/loan-applications/", json={
        "user_id": customer_id,
        "product_id": product_id,
        "requested_amount": 50000.0
    })
    app_id = create.json()["id"]

    response = client.put(f"/loan-applications/{app_id}/status", json={
        "status": "approved",
        "approved_amount": 50000.0,
        "processed_by": officer_id
    })
    assert response.status_code == 200
    assert response.json()["status"] == "approved"


def test_cannot_disburse_without_approval(client):
    """PDF Rule: cannot disburse unless status = approved"""
    customer_id = create_customer(client, "disburse@test.com")
    officer_id = create_officer(client, "disburseofficer@test.com")
    product_id = create_product(client, name="Disburse Product")

    create = client.post("/loan-applications/", json={
        "user_id": customer_id,
        "product_id": product_id,
        "requested_amount": 50000.0
    })
    app_id = create.json()["id"]

    # Try to disburse directly from pending (skipping approved)
    response = client.put(f"/loan-applications/{app_id}/status", json={
        "status": "disbursed",
        "processed_by": officer_id
    })
    assert response.status_code == 400
    assert "approved" in response.json()["detail"].lower()


def test_reject_application(client):
    """Loan officer can reject"""
    customer_id = create_customer(client, "reject@test.com")
    officer_id = create_officer(client, "rejectofficer@test.com")
    product_id = create_product(client, name="Reject Product")

    create = client.post("/loan-applications/", json={
        "user_id": customer_id,
        "product_id": product_id,
        "requested_amount": 50000.0
    })
    app_id = create.json()["id"]

    response = client.put(f"/loan-applications/{app_id}/status", json={
        "status": "rejected",
        "processed_by": officer_id
    })
    assert response.status_code == 200
    assert response.json()["status"] == "rejected"


def test_pagination(client):
    response = client.get("/loan-applications/?skip=0&limit=2")
    assert response.status_code == 200
    assert len(response.json()) <= 2