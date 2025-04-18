from app import app
from models import db

# Set up DB
with app.app_context():
    db.create_all()