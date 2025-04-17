import random
import json
from flask import request # type: ignore
from apiflask import APIBlueprint # type: ignore
from models import db, Character
from data import types, occupations, styles, dispositions, palettes, accessories

bp = APIBlueprint('characters', __name__)

@bp.get('/character')
def generate_character():
    character = {
        'type': random.choice(types),
        'occupation': random.choice(occupations),
        'style': random.choice(styles),
        'disposition': random.choice(dispositions),
        'palette': random.choice(palettes),
        'accessory': random.choice(accessories)
    }
    return character

@bp.post('/character')
def save_character():
    data = request.json
    required = ['type', 'occupation', 'style', 'disposition', 'palette', 'accessory']
    if not all(key in data for key in required):
        return {'error': 'Missing required fields'}, 400

    recent = Character.query.filter_by(is_example=False).order_by(Character.created_at.asc()).all()
    if len(recent) >= 5:
        db.session.delete(recent[0])

    character = Character(
        type=data['type'],
        occupation=data['occupation'],
        style=data['style'],
        disposition=data['disposition'],
        palette=json.dumps(data['palette']),
        accessory=data['accessory'],
        is_example=False
    )
    db.session.add(character)
    db.session.commit()

    return {'message': 'Character saved successfully'}, 201