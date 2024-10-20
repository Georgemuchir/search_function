from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def init_db(app):
    db.init_app(app)
    ma.init_app(app)

    # Import models inside the function
    from models import User, Book

    return db, ma
