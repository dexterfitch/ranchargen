import pytest # type: ignore

def test_missing_token(client):
    response = client.get("/characteristics/admin")  # No token
    assert response.status_code == 403

def test_invalid_token(client):
    response = client.get("/characteristics/admin", headers={"x-admin-token": "wrong-token"})
    assert response.status_code == 403

def test_valid_admin_token(client, admin_headers):
    response = client.get("/characteristics/admin", headers=admin_headers)
    assert response.status_code == 200