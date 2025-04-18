from flask import request  # type: ignore
from apiflask import APIBlueprint  # type: ignore
from models import db, Character, Palette
from utils import require_admin_token

bp = APIBlueprint('examples', __name__)

@bp.get('/examples')
def get_examples():
    examples = Character.query.filter_by(is_example=True).all()
    return {'examples': [c.serialize() for c in examples]}

@bp.get('/examples/admin')
@require_admin_token
def get_all_examples_with_ids():
    examples = Character.query.filter_by(is_example=True).order_by(Character.id.asc()).all()
    return {'examples': [c.serialize() for c in examples]}

@bp.post('/examples')
@require_admin_token
def add_example():
    data = request.json
    required = ['type', 'occupation', 'style', 'disposition', 'palette', 'accessory']
    if not all(key in data for key in required):
        return {'error': 'Missing required fields'}, 400

    # Validate palette
    palette_data = data['palette']
    if not isinstance(palette_data, dict) or "name" not in palette_data:
        return {'error': 'Palette must include a valid name.'}, 400

    palette_entry = Palette.query.filter_by(name=palette_data["name"]).first()
    if not palette_entry:
        return {'error': f"Palette '{palette_data['name']}' not found."}, 400

    character = Character(
        type=data['type'],
        occupation=data['occupation'],
        style=data['style'],
        disposition=data['disposition'],
        palette=palette_entry.colors,  # store as JSON string
        accessory=data['accessory'],
        is_example=True
    )
    db.session.add(character)
    db.session.commit()

    return {'message': 'Example character added successfully'}, 201

@bp.put('/examples/<int:id>')
@require_admin_token
def update_example(id):
    data = request.json
    required = ['type', 'occupation', 'style', 'disposition', 'palette', 'accessory']
    if not all(key in data for key in required):
        return {'error': 'Missing required fields'}, 400

    character = Character.query.get(id)
    if not character or not character.is_example:
        return {'error': 'Example character not found'}, 404

    # Validate palette
    palette_data = data['palette']
    if not isinstance(palette_data, dict) or "name" not in palette_data:
        return {'error': 'Palette must include a valid name.'}, 400

    palette_entry = Palette.query.filter_by(name=palette_data["name"]).first()
    if not palette_entry:
        return {'error': f"Palette '{palette_data['name']}' not found."}, 400

    # Update fields
    character.type = data['type']
    character.occupation = data['occupation']
    character.style = data['style']
    character.disposition = data['disposition']
    character.palette = palette_entry.colors
    character.accessory = data['accessory']

    db.session.commit()
    return {'message': 'Example character updated successfully'}, 200

@bp.delete('/examples/<int:id>')
@require_admin_token
def delete_example(id):
    character = Character.query.get(id)
    if not character or not character.is_example:
        return {'error': 'Example character not found'}, 404

    db.session.delete(character)
    db.session.commit()
    return {'message': 'Example character deleted'}, 200