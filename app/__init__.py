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

from app.routes import vehicles, auth, motorcycles, sells
app.register_blueprint(vehicles.vehicles_bp)
app.register_blueprint(sells.sells_bp)
app.register_blueprint(motorcycles.motorcycles_bp)
app.register_blueprint(auth.auth_bp)
