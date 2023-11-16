# config.py

import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:N0p0dras@localhost/proline'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key'
