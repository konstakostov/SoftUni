import os
import django
from django.db.models import Q, Count, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Director, Actor, Movie


# Create and run your queries within functions
def get_directors(search_name=None, search_nationality=None):
    directors = None

    if not search_name and not search_nationality:
        return ""

    elif search_name and search_nationality:
        directors = Director.objects.filter(
            Q(full_name__icontains=search_name) &
            Q(nationality__icontains=search_nationality)
        ).order_by(
            'full_name'
        )

    elif search_name and not search_nationality:
        directors = Director.objects.filter(
            Q(full_name__icontains=search_name)
        ).order_by(
            'full_name'
        )

    elif not search_name and search_nationality:
        directors = Director.objects.filter(
            Q(nationality__icontains=search_nationality)
        ).order_by(
            'full_name'
        )

    if not directors:
        return ""

    result = []

    for director in directors:
        result.append(
            f"Director: {director.full_name}, "
            f"nationality: {director.nationality}, "
            f"experience: {director.years_of_experience}"
        )

    return '\n'.join(result)


def get_top_director():
    top_director = Director.objects.annotate(
            total_movies_count=Count('movies_directed'),
        ).order_by(
            '-total_movies_count',
            'full_name',
        ).first()

    if not top_director:
        return ""

    return f"Top Director: {top_director.full_name}, movies: {top_director.total_movies_count}."


def get_top_actor():
    top_actor = Actor.objects.annotate(
        movies_made=Count('movies_starred'),
    ).order_by(
        '-movies_made',
        'full_name',
    ).first()

    if not top_actor or top_actor.movies_made == 0:
        return ""

    movies_list = []
    movies_total_rating = 0

    for movie in top_actor.movies_starred.all():
        movies_list.append(movie.title)

        movies_total_rating += movie.rating

    movies_avg_rating = movies_total_rating / len(movies_list)

    return (f"Top Actor: {top_actor.full_name}, "
            f"starring in movies: {', '.join(movies_list)}, "
            f"movies average rating: {movies_avg_rating:.1f}")


def get_actors_by_movies_count():
    top_actors = Actor.objects.annotate(
        movies_made=Count('movies_participated'),
    ).order_by(
        '-movies_made',
        'full_name',
    )[:3]

    if not top_actors or top_actors[0].movies_made == 0:
        return ""

    result = []

    for actor in top_actors:
        result.append(
            f"{actor.full_name}, "
            f"participated in {actor.movies_made} movies"
        )

    return '\n'.join(result)


def get_top_rated_awarded_movie():
    top_movie = Movie.objects.filter(
        is_awarded=True,
    ).order_by(
        '-rating',
        'title',
    ).first()

    if not top_movie:
        return ""

    movie_title = top_movie.title
    movie_rating = top_movie.rating
    starring_actor_full_name = "N/A"
    cast = "N/A"

    if top_movie.starring_actor:
        starring_actor_full_name = top_movie.starring_actor.full_name

    participating_actors = []
    for actor in top_movie.actors.order_by('full_name'):
        participating_actors.append(actor.full_name)

    if participating_actors:
        cast = ', '.join(participating_actors)

    return (f"Top rated awarded movie: {movie_title}, "
            f"rating: {movie_rating:.1f}."
            f" Starring actor: {starring_actor_full_name}. "
            f"Cast: {cast}.")


def increase_rating():
    updated_movies = Movie.objects.filter(
        is_classic=True,
        rating__lt=10.0,
    ).update(
        rating=F('rating') + 0.1
    )

    if not updated_movies:
        return "No ratings increased."

    return f"Rating increased for {updated_movies} movies."
