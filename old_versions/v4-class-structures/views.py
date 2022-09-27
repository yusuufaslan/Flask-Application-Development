from datetime import datetime
from flask import render_template, current_app, abort


def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)


def movies_page():
    db = current_app.config["db"]
    movies = db.get_movies()
    return render_template("movies.html", movies=sorted(movies))


def movie_page(movie_key):
    db = current_app.config["db"]
    movie = db.get_movie(movie_key)

    if movie is None:
        abort(404)

    return render_template("movie.html", movie=movie)
