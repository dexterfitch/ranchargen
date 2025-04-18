from .db import db
import json

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    occupation = db.Column(db.String(50))
    style = db.Column(db.String(50))
    disposition = db.Column(db.String(50))
    palette = db.Column(db.Text)
    accessory = db.Column(db.String(100))
    is_example = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "occupation": self.occupation,
            "style": self.style,
            "disposition": self.disposition,
            "palette": json.loads(self.palette) if self.palette else [],
            "accessory": self.accessory,
            "is_example": self.is_example,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
