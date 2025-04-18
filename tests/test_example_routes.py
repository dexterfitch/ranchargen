import pytest # type: ignore
from models import Character, Palette

def test_add_example(client, app, admin_headers):
    with app.app_context():
        palette = Palette.query.first()
        assert palette is not None

    payload = {
        "type": "ghost",
        "occupation": "bard",
        "style": "gothic",
        "disposition": "melancholy",
        "palette": {"name": palette.name},
        "accessory": "a tattered book"
    }

    response = client.post("/examples", json=payload, headers=admin_headers)
    assert response.status_code in (201, 409)

def test_get_examples_admin(client, admin_headers):
    response = client.get("/examples/admin", headers=admin_headers)
    assert response.status_code == 200
    assert isinstance(response.json.get("examples"), list)

def test_update_example(client, app, admin_headers):
    with app.app_context():
        example = Character.query.filter_by(type="ghost", is_example=True).first()
        assert example is not None
        example_id = example.id

        palette = Palette.query.first()
        assert palette is not None

    updated = {
        "type": "ghost",
        "occupation": "bard",
        "style": "gothic",
        "disposition": "mischievous",
        "palette": {"name": palette.name},
        "accessory": "a cursed fiddle"
    }

    response = client.put(f"/examples/{example_id}", json=updated, headers=admin_headers)
    assert response.status_code == 200

def test_delete_example(client, app, admin_headers):
    with app.app_context():
        example = Character.query.filter_by(type="ghost", is_example=True).first()
        assert example is not None
        example_id = example.id

    response = client.delete(f"/examples/{example_id}", headers=admin_headers)
    assert response.status_code == 200