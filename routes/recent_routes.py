from apiflask import APIBlueprint  # type: ignore
from models import db, Character
from sqlalchemy import desc  # type: ignore
from utils import require_admin_token

bp = APIBlueprint("recent", __name__)

@bp.get("/recent")
def get_recent_characters():
    recent = Character.query.filter_by(is_example=False)\
                            .order_by(desc(Character.created_at))\
                            .limit(5).all()
    return {"recent": [c.serialize() for c in recent]}

@bp.delete("/recent/<int:id>")
@require_admin_token
def delete_recent_character(id):
    character = db.session.get(Character, id)

    if not character or character.is_example:
        return {"error": "Recent character not found"}, 404

    db.session.delete(character)
    db.session.commit()
    return {"message": f"Deleted recent character with ID {id}"}, 200

@bp.delete("/recent")
@require_admin_token
def delete_all_recent_characters():
    recent_characters = Character.query.filter_by(is_example=False).all()

    if not recent_characters:
        return {"message": "No recent characters to delete"}, 200

    for character in recent_characters:
        db.session.delete(character)

    db.session.commit()
    return {"message": f"Deleted {len(recent_characters)} recent characters"}, 200
