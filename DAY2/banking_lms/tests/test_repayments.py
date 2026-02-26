"""
Tests for Repayment endpoints
POST /repayments
GET  /loan-applications/{id}/repayments

Also tests:
- Only disbursed loans can receive repayments
- Loan auto-closes after full repayment
"""


# ── Helper to create a fully disbursed loan ─────────────────
def setup_disbursed_loan(client, suffix=""):
    """Creates customer, officer, product, application, approves and disburses it"""
    customer = client.post("/users/", json={
        "name": "Repay Customer",
        "email": f"repaycust{suffix}@test.com",
        "role": "customer",
        "password": "pass123"
    }).json()["id"]

    officer = client.post("/users/", json={
        "name": "Repay Officer",
        "email": f"repayofficer{suffix}@test.com",
        "role": "loan_officer",
        "password": "pass123"
    }).json()["id"]

    product = client.post("/loan-products/", json={
        "product_name": f"Repay Product {suffix}",
        "interest_rate": 10.0,
        "max_amount": 100000.0,
        "tenure_months": 12
    }).json()["id"]

    app = client.post("/loan-applications/", json={
        "user_id": customer,
        "product_id": product,
        "requested_amount": 50000.0
    }).json()["id"]

    # Approve
    client.put(f"/loan-applications/{app}/status", json={
        "status": "approved",
        "approved_amount": 50000.0,
        "processed_by": officer
    })

    # Disburse
    client.put(f"/loan-applications/{app}/status", json={
        "status": "disbursed",
        "processed_by": officer
    })

    return app  # return the loan application id


# ── Tests ────────────────────────────────────────────────────

def test_add_repayment(client):
    app_id = setup_disbursed_loan(client, "1")

    response = client.post("/repayments", json={
        "loan_application_id": app_id,
        "amount_paid": 10000.0,
        "payment_date": "2026-03-01"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["loan_application_id"] == app_id
    assert data["amount_paid"] == 10000.0
    assert data["payment_status"] == "completed"


def test_get_repayments_by_loan(client):
    app_id = setup_disbursed_loan(client, "2")

    # Add two repayments
    client.post("/repayments", json={
        "loan_application_id": app_id,
        "amount_paid": 10000.0,
        "payment_date": "2026-03-01"
    })
    client.post("/repayments", json={
        "loan_application_id": app_id,
        "amount_paid": 10000.0,
        "payment_date": "2026-04-01"
    })

    response = client.get(f"/loan-applications/{app_id}/repayments")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_repayment_on_pending_loan_blocked(client):
    """PDF Rule: repayment only allowed on disbursed loans"""
    customer = client.post("/users/", json={
        "name": "Pending Customer",
        "email": "pendingcust@test.com",
        "role": "customer",
        "password": "pass123"
    }).json()["id"]

    product = client.post("/loan-products/", json={
        "product_name": "Pending Product",
        "interest_rate": 10.0,
        "max_amount": 100000.0,
        "tenure_months": 12
    }).json()["id"]

    # Application stays in pending status
    app = client.post("/loan-applications/", json={
        "user_id": customer,
        "product_id": product,
        "requested_amount": 50000.0
    }).json()["id"]

    response = client.post("/repayments", json={
        "loan_application_id": app,
        "amount_paid": 10000.0,
        "payment_date": "2026-03-01"
    })
    assert response.status_code == 400
    assert "disbursed" in response.json()["detail"].lower()


def test_loan_auto_closes_after_full_repayment(client):
    """PDF Rule: loan closes only after full repayment"""
    app_id = setup_disbursed_loan(client, "3")

    # Pay full approved amount (50000)
    client.post("/repayments", json={
        "loan_application_id": app_id,
        "amount_paid": 25000.0,
        "payment_date": "2026-03-01"
    })
    client.post("/repayments", json={
        "loan_application_id": app_id,
        "amount_paid": 25000.0,
        "payment_date": "2026-04-01"
    })

    # Check loan status - should be closed now
    response = client.get(f"/loan-applications/{app_id}")
    assert response.status_code == 200
    assert response.json()["status"] == "closed"


def test_repayment_invalid_loan(client):
    """Cannot add repayment to non-existent loan"""
    response = client.post("/repayments", json={
        "loan_application_id": 99999,
        "amount_paid": 10000.0,
        "payment_date": "2026-03-01"
    })
    assert response.status_code == 404