# models.py
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    genre = db.Column(db.String(100))
    release_year = db.Column(db.Integer)
    rating = db.Column(db.Float)

    def __init__(self, title, description, genre, release_year, rating):
        self.title = title
        self.description = description
        self.genre = genre
        self.release_year = release_year
        self.rating = rating

class MovieSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Movie
        load_instance = True
