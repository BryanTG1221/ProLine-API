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

CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

from app.routes import vehicles, auth, motorcycles, sells, users, brands

app.register_blueprint(brands.brands_bp)
app.register_blueprint(sells.sells_bp)
app.register_blueprint(users.users_bp)
app.register_blueprint(vehicles.vehicles_bp)
app.register_blueprint(motorcycles.motorcycles_bp)
app.register_blueprint(auth.auth_bp)
