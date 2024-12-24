# app.py
from flask import Flask
from config import Config
from models import db
from resources import movie_bp

app = Flask(__name__)
app.config.from_object(Config)

# Инициализируем базу данных и Marshmallow
db.init_app(app)

# Регистрация маршрутов
app.register_blueprint(movie_bp)

@app.before_request
def create_tables():
    db.create_all()
    app.before_request_funcs[None].remove(create_tables)


if __name__ == '__main__':
    app.run(debug=False)
