from app import app
from models import db, Characteristic, Palette
import json

with app.app_context():
    # Clear tables
    Characteristic.query.delete()
    Palette.query.delete()

    # Seed characteristics
    characteristics = {
        "type": ["slime", "elf", "android", "human", "goblin"],
        "occupation": ["baker", "warrior", "gardener", "detective", "poet"],
        "style": ["vintage", "cyberpunk", "furs", "cottagecore", "steampunk"],
        "disposition": ["sunny", "brooding", "curious", "mischievous", "stoic"],
        "accessory": ["a glowing orb", "a pocket watch", "a tattered book", "a lucky feather", "a broken umbrella"]
    }

    for category, names in characteristics.items():
        for name in names:
            db.session.add(Characteristic(name=name, category=category))

    # Seed palettes
    palettes = [
        {
            "name": "Tropical Fruit",
            "colors": ["#FFB347", "#FF6961", "#FF33CC"]
        },
        {
            "name": "Moonlight Garden",
            "colors": ["#2C3E50", "#4CA1AF", "#C4E0E5"]
        },
        {
            "name": "Rustic Autumn",
            "colors": ["#C1440E", "#D9BF77", "#4C3A32"]
        },
        {
            "name": "Pastel Dream",
            "colors": ["#FADADD", "#D1CFE2", "#B5EAD7"]
        },
        {
            "name": "Neon Arcade",
            "colors": ["#FF00FF", "#00FFFF", "#FFFF00"]
        }
    ]

    for p in palettes:
        db.session.add(Palette(name=p["name"], colors=json.dumps(p["colors"])))

    db.session.commit()
    print("Database seeded successfully.")
