import json
from flask import request
from apiflask import APIBlueprint
from models import db, Character

bp = APIBlueprint('examples', __name__)

@bp.get('/examples')
def get_examples():
    characters = Character.query.filter_by(is_example=True).all()

    return {'examples': [
        {
            'type': c.type,
            'occupation': c.occupation,
            'style': c.style,
            'disposition': c.disposition,
            'palette': json.loads(c.palette),
            'accessory': c.accessory
        } for c in characters
    ]}

@bp.post('/examples')
def add_example():
    data = request.json
    required = ['type', 'occupation', 'style', 'disposition', 'palette', 'accessory']
    if not all(key in data for key in required):
        return {'error': 'Missing required fields'}, 400

    character = Character(
        type=data['type'],
        occupation=data['occupation'],
        style=data['style'],
        disposition=data['disposition'],
        palette=json.dumps(data['palette']),
        accessory=data['accessory'],
        is_example=True
    )
    db.session.add(character)
    db.session.commit()

    return {'message': 'Example character added successfully'}, 201