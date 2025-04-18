import os
from apiflask import APIFlask # type: ignore
from models import db

from routes.character_routes import bp as character_bp
from routes.category_routes import bp as category_bp
from routes.recent_routes import bp as recent_bp
from routes.example_routes import bp as example_bp
from routes.characteristics_routes import bp as characteristics_bp

app = APIFlask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register blueprints
app.register_blueprint(character_bp)
app.register_blueprint(category_bp)
app.register_blueprint(recent_bp)
app.register_blueprint(example_bp)
app.register_blueprint(characteristics_bp)

if __name__ == '__main__':
    app.run(debug=True)