from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)

CORS(app, resources={r"/api/*": {"origins": "*"}})

# Registrar blueprints después de definir db
from app.routes import vehicles, auth, motorcycles
app.register_blueprint(vehicles.vehicles_bp)
app.register_blueprint(motorcycles.motorcycles_bp)
app.register_blueprint(auth.auth_bp)
