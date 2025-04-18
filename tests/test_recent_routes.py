import pytest # type: ignore
from models import Character

def test_generate_and_save_character(client):
    payload = {
        "type": "slime",
        "occupation": "baker",
        "style": "furs",
        "disposition": "sunny",
        "palette": {"name": "Tropical Fruit"},
        "accessory": "a tattered book"
    }
    response = client.post("/character", json=payload)
    assert response.status_code == 201

def test_get_recent(client):
    response = client.get("/recent")
    assert response.status_code == 200
    assert "recent" in response.json

def test_delete_individual_recent(client, app, admin_headers):
    with app.app_context():
        character = Character.query.filter_by(is_example=False).first()
        assert character is not None
        character_id = character.id

    response = client.delete(f"/recent/{character_id}", headers=admin_headers)
    assert response.status_code == 200

def test_delete_all_recent(client, admin_headers):
    response = client.delete("/recent", headers=admin_headers)
    assert response.status_code == 200