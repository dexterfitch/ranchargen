import pytest # type: ignore
from models.characteristic import Characteristic

def test_get_characteristics_admin(client, admin_headers):
    response = client.get("/characteristics/admin", headers=admin_headers)
    assert response.status_code == 200
    assert "occupation" in response.json

def test_add_characteristic(client, admin_headers):
    new_data = {"name": "mushroom farmer", "category": "occupation"}
    response = client.post("/characteristics", json=new_data, headers=admin_headers)

    if response.status_code == 409:
        assert "already exists" in response.json["error"]
    else:
        assert response.status_code == 201

def test_edit_characteristic(client, app, admin_headers):
    with app.app_context():
        char = Characteristic.query.filter_by(name="necromancer").first()
        assert char is not None
        char_id = char.id

    updated = {"name": "bone wizard", "category": "occupation"}
    response = client.put(f"/characteristics/{char_id}", json=updated, headers=admin_headers)
    assert response.status_code == 200

def test_delete_characteristic(client, app, admin_headers):
    with app.app_context():
        char = Characteristic.query.filter_by(name="necromancer").first()
        assert char is not None
        char_id = char.id

    response = client.delete(f"/characteristics/{char_id}", headers=admin_headers)
    assert response.status_code == 200