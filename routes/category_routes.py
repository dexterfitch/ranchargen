from apiflask import APIBlueprint # type: ignore
from models.characteristic import Characteristic
from models.palette import Palette
from sqlalchemy import asc  # type: ignore

bp = APIBlueprint("categories", __name__)

@bp.get("/types")
def get_types():
    results = Characteristic.query.filter_by(category="type").order_by(asc(Characteristic.name)).all()
    return {"types": [c.name for c in results]}

@bp.get("/occupations")
def get_occupations():
    results = Characteristic.query.filter_by(category="occupation").order_by(asc(Characteristic.name)).all()
    return {"occupations": [c.name for c in results]}

@bp.get("/styles")
def get_styles():
    results = Characteristic.query.filter_by(category="style").order_by(asc(Characteristic.name)).all()
    return {"styles": [c.name for c in results]}

@bp.get("/dispositions")
def get_dispositions():
    results = Characteristic.query.filter_by(category="disposition").order_by(asc(Characteristic.name)).all()
    return {"dispositions": [c.name for c in results]}

@bp.get("/palettes")
def get_palettes():
    results = Palette.query.order_by(asc(Palette.name)).all()
    return {"palettes": [p.to_dict() for p in results]}

@bp.get("/accessories")
def get_accessories():
    results = Characteristic.query.filter_by(category="accessory").order_by(asc(Characteristic.name)).all()
    return {"accessories": [c.name for c in results]}