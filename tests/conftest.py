import os
import json
import pytest  # type: ignore
from dotenv import load_dotenv  # type: ignore
from app import app as flask_app
from models import db
from models.character import Character
from models.characteristic import Characteristic
from models.palette import Palette

# Get base directory
basedir = os.path.abspath(os.path.dirname(__file__))
test_db_path = os.path.join(basedir, "test.db")

# Load environment variables
load_dotenv()

# Use the loaded admin token from .env
ADMIN_HEADERS = {"x-admin-token": os.getenv("ADMIN_TOKEN", "")}

@pytest.fixture
def app():
    flask_app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///" + test_db_path,
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    })

    with flask_app.app_context():
        if os.path.exists(test_db_path):
            os.remove(test_db_path)
        db.create_all()
        yield flask_app
        db.session.remove()
        db.drop_all()
        if os.path.exists(test_db_path):
            os.remove(test_db_path)

@pytest.fixture(autouse=True)
def seed_data(app):
    with app.app_context():
        categories = {
            "type": ["ghost", "slime", "imp"],
            "occupation": ["bard", "baker", "necromancer"],
            "style": ["gothic", "furs"],
            "disposition": ["melancholy", "sunny"],
            "accessory": ["a tattered book", "bone flute"]
        }

        for category, names in categories.items():
            for name in names:
                db.session.add(Characteristic(name=name, category=category))

        palettes = [
            {
                "name": "Tropical Fruit",
                "colors": json.dumps(["#FF6F61", "#FFD662", "#6B5B95"])
            },
            {
                "name": "Ghost Glow",
                "colors": json.dumps(["#E0E4CC", "#69D2E7", "#FAFAFA"])
            }
        ]

        for p in palettes:
            db.session.add(Palette(name=p["name"], colors=p["colors"]))

        db.session.commit()

        example_character = Character(
            type="ghost",
            occupation="bard",
            style="gothic",
            disposition="melancholy",
            palette=json.dumps(["#E0E4CC", "#69D2E7", "#FAFAFA"]),
            accessory="a tattered book",
            is_example=True
        )
        db.session.add(example_character)

        recent_character = Character(
            type="slime",
            occupation="baker",
            style="furs",
            disposition="sunny",
            palette=json.dumps(["#FF6F61", "#FFD662", "#6B5B95"]),
            accessory="bone flute",
            is_example=False
        )
        db.session.add(recent_character)

        db.session.commit()

@pytest.fixture
def admin_headers():
    token = os.getenv("ADMIN_TOKEN", "")
    return {"x-admin-token": token}

@pytest.fixture
def client(app):
    return app.test_client()