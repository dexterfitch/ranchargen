from apiflask import APIBlueprint

bp = APIBlueprint('examples', __name__)

@bp.get('/examples')
def get_examples():
    examples = [
        {
            'type': 'dragonling',
            'occupation': 'relic hunter',
            'style': 'steampunk',
            'disposition': 'mischievous',
            'palette': ['#8B0000', '#DAA520', '#5F9EA0'],
            'accessory': 'a mechanical gauntlet'
        },
        {
            'type': 'slime',
            'occupation': 'street‑food vendor',
            'style': 'cyberpunk',
            'disposition': 'serene',
            'palette': ['#0FF0FC', '#FF10F0', '#39FF14'],
            'accessory': 'a levitating lantern'
        }
    ]
    return {'examples': examples}