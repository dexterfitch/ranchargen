from apiflask import APIBlueprint
from data import types, occupations, styles, dispositions, palettes, accessories

bp = APIBlueprint('categories', __name__)

@bp.get('/types')
def get_types():
    return {'types': types}

@bp.get('/occupations')
def get_occupations():
    return {'occupations': occupations}

@bp.get('/styles')
def get_styles():
    return {'styles': styles}

@bp.get('/dispositions')
def get_dispositions():
    return {'dispositions': dispositions}

@bp.get('/palettes')
def get_palettes():
    return {'palettes': palettes}

@bp.get('/accessories')
def get_accessories():
    return {'accessories': accessories}