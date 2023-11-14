# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)

from app.routes import vehicles, auth

# Registrar blueprints
app.register_blueprint(vehicles.vehicles_bp, url_prefix='/vehicles')
app.register_blueprint(auth.auth_bp, url_prefix='/auth')
