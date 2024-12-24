# resources.py
from flask import Blueprint, request, jsonify
from models import db, Movie, MovieSchema

movie_bp = Blueprint('movie', __name__)


# Создание нового фильма
@movie_bp.route('/movies', methods=['POST'])
def add_movie():
    title = request.json.get('title')
    description = request.json.get('description')
    genre = request.json.get('genre')
    release_year = request.json.get('release_year')
    rating = request.json.get('rating')

    new_movie = Movie(title=title, description=description, genre=genre,
                      release_year=release_year, rating=rating)

    db.session.add(new_movie)
    db.session.commit()

    return MovieSchema().jsonify(new_movie), 201


# Получение списка всех фильмов
@movie_bp.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return MovieSchema(many=True).jsonify(movies)


# Получение информации о фильме по ID
@movie_bp.route('/movies/<int:id>', methods=['GET'])
def get_movie(id):
    movie = Movie.query.get_or_404(id)
    return MovieSchema().jsonify(movie)


# Обновление данных о фильме
@movie_bp.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    movie = Movie.query.get_or_404(id)

    movie.title = request.json.get('title', movie.title)
    movie.description = request.json.get('description', movie.description)
    movie.genre = request.json.get('genre', movie.genre)
    movie.release_year = request.json.get('release_year', movie.release_year)
    movie.rating = request.json.get('rating', movie.rating)

    db.session.commit()

    return MovieSchema().jsonify(movie)


# Удаление фильма
@movie_bp.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    movie = Movie.query.get_or_404(id)
    db.session.delete(movie)
    db.session.commit()
    return '', 204
