import random
from flask import request  # type: ignore
from apiflask import APIBlueprint  # type: ignore
from sqlalchemy.sql.expression import func  # type: ignore
from models import Character, Characteristic, Palette, db
from utils import require_admin_token

bp = APIBlueprint('characters', __name__)

def get_random_characteristic(category):
    result = Characteristic.query.filter_by(category=category).order_by(func.random()).first()
    return result.name if result else None

def validate_character_input(data):
    required = ['type', 'occupation', 'style', 'disposition', 'palette', 'accessory']
    if not all(key in data for key in required):
        return False, {'error': 'Missing required fields'}, 400

    for field in ['type', 'occupation', 'style', 'disposition', 'accessory']:
        if not Characteristic.query.filter_by(category=field, name=data[field]).first():
            return False, {'error': f"Invalid value for '{field}': {data[field]}"}, 400

    palette_data = data.get('palette')
    if not isinstance(palette_data, dict) or "name" not in palette_data:
        return False, {'error': 'Palette must include a valid name.'}, 400

    palette = Palette.query.filter_by(name=palette_data["name"]).first()
    if not palette:
        return False, {'error': f"Palette '{palette_data['name']}' not found."}, 400

    return True, palette, None

@bp.get('/character')
def generate_character():
    palette_row = Palette.query.order_by(func.random()).first()
    palette = palette_row.to_dict() if palette_row else None

    return {
        "type": get_random_characteristic("type"),
        "occupation": get_random_characteristic("occupation"),
        "style": get_random_characteristic("style"),
        "disposition": get_random_characteristic("disposition"),
        "palette": palette,
        "accessory": get_random_characteristic("accessory")
    }

@bp.get('/characters/<int:id>')
@require_admin_token
def get_character_by_id(id):
    character = db.session.get(Character, id)
    if not character:
        return {'error': 'Character not found'}, 404

    return character.serialize()

@bp.get('/characters/admin')
@require_admin_token
def get_all_characters():
    characters = Character.query.order_by(Character.created_at.desc()).all()
    return {'characters': [char.serialize() for char in characters]}

@bp.post('/character')
def save_character():
    data = request.json
    valid, palette_or_response, error_code = validate_character_input(data)
    if not valid:
        return palette_or_response, error_code

    # Keep only last 5 recent characters
    recent = Character.query.filter_by(is_example=False).order_by(Character.created_at.asc()).all()
    if len(recent) >= 5:
        db.session.delete(recent[0])

    new_character = Character(
        type=data['type'],
        occupation=data['occupation'],
        style=data['style'],
        disposition=data['disposition'],
        palette=palette_or_response.colors,  # JSON string
        accessory=data['accessory'],
        is_example=False
    )
    db.session.add(new_character)
    db.session.commit()

    return {'message': 'Character saved successfully'}, 201