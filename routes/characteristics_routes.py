from apiflask import APIBlueprint
from data import types, occupations, styles, dispositions, palettes, accessories

bp = APIBlueprint('characteristics', __name__)

@bp.get('/characteristics')
def get_all_characteristics():
    return {
        'type': types,
        'occupation': occupations,
        'style': styles,
        'disposition': dispositions,
        'palette': palettes,
        'accessory': accessories
    }