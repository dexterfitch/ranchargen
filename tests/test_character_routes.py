import json
import pytest # type: ignore
from models.character import Character

def test_generate_character(client):
    response = client.get("/character")
    assert response.status_code == 200
    data = response.json
    assert all(key in data for key in ["type", "occupation", "style", "disposition", "palette", "accessory"])
    assert isinstance(data["palette"], dict)
    assert "name" in data["palette"]
    assert "colors" in data["palette"]

def test_save_character_valid(client, app):
    with app.app_context():
        palette = next((p for p in ["Tropical Fruit", "Fire & Brimstone", "Lavender Parade"]
                        if p), None)
        assert palette is not None

    payload = {
        "type": "slime",
        "occupation": "baker",
        "style": "furs",
        "disposition": "sunny",
        "palette": { "name": "Tropical Fruit" },
        "accessory": "a tattered book"
    }

    response = client.post("/character", data=json.dumps(payload), content_type="application/json")
    assert response.status_code == 201
    assert response.json["message"] == "Character saved successfully"

def test_get_character_by_id(client, app, admin_headers):
    with app.app_context():
        # Get any existing character (either recent or example)
        character = Character.query.first()
        assert character is not None
        character_id = character.id

    response = client.get(f"/characters/{character_id}", headers=admin_headers)
    assert response.status_code == 200
    data = response.json
    assert data["id"] == character_id
    assert "type" in data
    assert "palette" in data

def test_get_character_by_invalid_id(client, admin_headers):
    response = client.get("/characters/9999", headers=admin_headers)
    assert response.status_code == 404
    assert "error" in response.json
    assert response.json["error"] == "Character not found"
