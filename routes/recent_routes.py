import json
from apiflask import APIBlueprint
from models import Character
from sqlalchemy import desc

bp = APIBlueprint('recent', __name__)

@bp.get('/recent')
def get_recent_characters():
    characters = Character.query.filter_by(is_example=False).order_by(desc(Character.created_at)).limit(5).all()

    return {'recent': [
        {
            'type': c.type,
            'occupation': c.occupation,
            'style': c.style,
            'disposition': c.disposition,
            'palette': json.loads(c.palette),
            'accessory': c.accessory
        } for c in characters
    ]}