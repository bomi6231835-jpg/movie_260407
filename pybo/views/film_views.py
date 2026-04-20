from flask import Blueprint, render_template, jsonify
from pybo.models import Movie

bp = Blueprint('film', __name__, url_prefix='/film')

@bp.route('/event', methods=['GET'])
def event():
    return render_template('event.html')

@bp.route('/movie/list', methods=['GET'])
def movie_list():
    movies = Movie.query.all()
    return render_template('movie_list.html', movies=movies)

@bp.route('/movie/<int:movie_id>', methods=['GET'])
def movie_info(movie_id):
    movie = Movie.query.filter_by(tmdb_id=movie_id).first()
    return render_template('movie_info/movie_info_1.html', movie=movie)

@bp.route('/booking/<int:movie_id>', methods=['GET','POST'])
def booking(movie_id):
    movies = Movie.query.all()
    movie = Movie.query.filter_by(tmdb_id=movie_id).first()
    return render_template('booking.html', movie_id=movie_id, movies=movies, movie=movie)

@bp.route('/person/seat', methods=['GET','POST'])
def person_seat():
    return render_template('person_seat.html')


