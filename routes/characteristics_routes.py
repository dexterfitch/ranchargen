from flask import request  # type: ignore
from apiflask import APIBlueprint  # type: ignore
from sqlalchemy import asc  # type: ignore
from models import db, Characteristic, Palette
from utils import require_admin_token

bp = APIBlueprint("characteristics", __name__)

@bp.get("/characteristics")
def get_all_characteristics():
    characteristics = Characteristic.query.order_by(
        asc(Characteristic.category), asc(Characteristic.name)
    ).all()

    grouped = {}
    for c in characteristics:
        grouped.setdefault(c.category, []).append(c.name)

    palettes = Palette.query.order_by(Palette.name).all()
    grouped["palette"] = [p.to_dict() for p in palettes]

    return grouped

@bp.get("/characteristics/admin")
@require_admin_token
def get_all_characteristics_with_ids():
    characteristics = Characteristic.query.order_by(
        asc(Characteristic.category), asc(Characteristic.name)
    ).all()

    grouped = {}
    for c in characteristics:
        grouped.setdefault(c.category, []).append(c.to_dict())

    return grouped

@bp.post("/characteristics")
@require_admin_token
def add_characteristic():
    data = request.json
    required = ["name", "category"]

    if not all(key in data for key in required):
        return {"error": "Missing name or category"}, 400

    name = data["name"].strip()
    category = data["category"].strip()

    existing = Characteristic.query.filter_by(name=name, category=category).first()
    if existing:
        return {"error": f"'{name}' already exists in '{category}'"}, 409

    new_characteristic = Characteristic(name=name, category=category)
    db.session.add(new_characteristic)
    db.session.commit()

    return {"message": f"Added '{name}' to '{category}'"}, 201

@bp.put("/characteristics/<int:id>")
@require_admin_token
def edit_characteristic(id):
    data = request.json
    required = ["name", "category"]

    if not all(key in data for key in required):
        return {"error": "Missing name or category"}, 400

    characteristic = db.session.get(Characteristic, id)
    if not characteristic:
        return {"error": "Characteristic not found"}, 404

    name = data["name"].strip()
    category = data["category"].strip()

    # Prevent duplicates (excluding current)
    exists = Characteristic.query.filter_by(name=name, category=category).first()
    if exists and exists.id != id:
        return {"error": f"'{name}' already exists in '{category}'"}, 409

    characteristic.name = name
    characteristic.category = category
    db.session.commit()

    return {"message": f"Updated characteristic to '{name}' in '{category}'"}, 200

@bp.delete("/characteristics/<int:id>")
@require_admin_token
def delete_characteristic(id):
    characteristic = db.session.get(Characteristic, id)
    if not characteristic:
        return {"error": "Characteristic not found"}, 404

    db.session.delete(characteristic)
    db.session.commit()

    return {"message": f"Deleted characteristic '{characteristic.name}' from '{characteristic.category}'"}, 200