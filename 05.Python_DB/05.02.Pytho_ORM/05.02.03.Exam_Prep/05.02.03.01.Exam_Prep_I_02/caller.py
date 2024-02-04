import os
import django
from django.db.models import Q, Count, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Director, Actor, Movie


def get_directors(search_name=None, search_nationality=None):
    directors = None

    if search_name is None and search_nationality is None:
        return ""

    elif search_name is not None and search_nationality is not None:
        directors = Director.objects.filter(
            Q(full_name__icontains=search_name) &
            Q(nationality__icontains=search_nationality)
        )

    elif search_name is not None and search_nationality is None:
        directors = Director.objects.filter(
            Q(full_name__icontains=search_name)
        )

    elif search_name is None and search_nationality is not None:
        directors = Director.objects.filter(
            Q(nationality__icontains=search_nationality)
        )

    if not directors:
        return ""

    result = []

    for director in directors.order_by('full_name'):
        result.append(
            f"Director: {director.full_name}, "
            f"nationality: {director.nationality}, "
            f"experience: {director.years_of_experience}"
        )

    return '\n'.join(result)


def get_top_director():
    top_director = Director.objects.annotate(
            movies_made=Count('movies_directed'),
        ).order_by(
            '-movies_made',
            'full_name',
        ).first()

    if not top_director:
        return ""

    return (f"Top Director: {top_director.full_name}, "
            f"movies: {top_director.movies_made}.")


def get_top_actor():
    top_actor = Actor.objects.annotate(
        movies_made=Count('movies_starred')
    ).order_by(
        '-movies_made',
        'full_name'
    ).first()

    if not top_actor or top_actor.movies_made == 0:
        return ""

    filmography = []

    movies_rating_total = 0

    for movie in top_actor.movies_starred.all():
        filmography.append(movie.title)

        movies_rating_total += movie.rating

    movies_average_rating = movies_rating_total / len(filmography)

    return (f"Top Actor: {top_actor.full_name}, "
            f"starring in movies: {', '.join(filmography)}, "
            f"movies average rating: {movies_average_rating:.1f}"
            )


def get_actors_by_movies_count():
    top_three_actors = Actor.objects.annotate(
        movies_made=Count('movies_played_in')
    ).order_by(
        '-movies_made',
        'full_name',
    )[:3]

    if not top_three_actors or top_three_actors[0].movies_made == 0:
        return ""

    result = []

    for actor in top_three_actors:
        result.append(
            f"{actor.full_name}, participated in {actor.movies_made} movies"
        )

    return '\n'.join(result)


def get_top_rated_awarded_movie():
    top_movie = Movie.objects.filter(
        is_awarded=True,
    ).order_by(
        '-rating',
        'title'
    ).first()

    if not top_movie:
        return ""

    movie_title = top_movie.title
    movie_rating = top_movie.rating
    starring_actor_full_name = "N/A"
    cast = "N/A"

    if top_movie.starring_actor:
        starring_actor_full_name = top_movie.starring_actor.full_name

    possible_actors = []
    for actor in top_movie.actors.order_by('full_name'):
        possible_actors.append(actor.full_name)

    if possible_actors:
        cast = ', '.join(possible_actors)

    return (f"Top rated awarded movie: {movie_title}, "
            f"rating: {movie_rating:.1f}. "
            f"Starring actor: {starring_actor_full_name}. "
            f"Cast: {cast}.")


def increase_rating():
    movies_for_update = Movie.objects.filter(
        is_classic=True,
        rating__lt=10.0,
    )

    if not movies_for_update:
        return "No ratings increased."

    all_updated_movies = movies_for_update.update(
        rating=F('rating') + 0.1
    )

    return f"Rating increased for {all_updated_movies} movies."
