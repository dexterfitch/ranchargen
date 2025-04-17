from flask_sqlalchemy import SQLAlchemy # type: ignore

db = SQLAlchemy()

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