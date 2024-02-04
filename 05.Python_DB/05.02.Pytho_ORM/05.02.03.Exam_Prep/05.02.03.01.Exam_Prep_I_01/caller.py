import os
import django
from django.db.models import Q, Count, Avg, F, Case, When

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Director, Actor, Movie


# Create and run your queries within functions
def get_directors(search_name=None, search_nationality=None):
    directors = None

    # Both arguments ara NOT available
    if search_name is None and search_nationality is None:
        return ""

    # Both arguments ara available
    elif search_name is not None and search_nationality is not None:
        directors = Director.objects.filter(
            Q(full_name__icontains=search_name) &
            Q(nationality__icontains=search_nationality)
        ).order_by(
            'full_name',
        )

    # Only search_name is available
    elif search_name is not None and search_nationality is None:
        directors = Director.objects.filter(
            Q(full_name__icontains=search_name)
        ).order_by(
            'full_name',
        )

    # Only search_nationality is available
    elif search_name is None and search_nationality is not None:
        directors = Director.objects.filter(
            Q(nationality__icontains=search_nationality)
        ).order_by(
            'full_name',
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
        movies_count=Count('movies_directed')
    ).order_by(
            '-movies_count',
            'full_name',
        ).first()

    if not top_director:
        return ""

    return f"Top Director: {top_director.full_name}, movies: {top_director.movies_count}."


def get_top_actor():
    top_actor = Actor.objects.annotate(
        movies_count=Count('movies_starred')
    ).order_by(
        '-movies_count',
        'full_name',
    ).first()

    if top_actor is None or top_actor.movies_count == 0:
        return ""

    movies_list = top_actor.movies_starred.all().values_list('title', flat=True)

    avg_rating = top_actor.movies_starred.aggregate(
        Avg('rating')
    )['rating__avg']

    return (f"Top Actor: {top_actor.full_name}, "
            f"starring in movies: {', '.join(movies_list)}, "
            f"movies average rating: {avg_rating:.1f}")


def get_actors_by_movies_count():
    top_actors = Actor.objects.annotate(
        movies_count=Count('movies_played')
    ).order_by(
        '-movies_count',
        'full_name',
    )[:3]

    if not top_actors or top_actors[0].movies_count == 0:
        return ""

    actors_info = []

    for actor in top_actors:
        actors_info.append(
            f"{actor.full_name}, "
            f"participated in {actor.movies_count} movies")

    return '\n'.join(actors_info)


def get_top_rated_awarded_movie():
    top_movie = Movie.objects.filter(
        is_awarded=True,
    ).order_by(
        '-rating',
        'title',
    ).first()

    if not top_movie:
        return ""

    if top_movie.starring_actor:
        actor_in_movie = top_movie.starring_actor.full_name
    else:
        actor_in_movie = "N/A"

    all_actors_movie = top_movie.actors.order_by('full_name')

    all_actors_list = []
    for actor in all_actors_movie:
        all_actors_list.append(actor.full_name)

    if all_actors_list:
        cast_movie = ', '.join(all_actors_list)
    else:
        cast_movie = "N/A"

    top_movie_rating = top_movie.rating

    return (f"Top rated awarded movie: {top_movie.title}, "
            f"rating: {top_movie_rating:.1f}. "
            f"Starring actor: {actor_in_movie}. "
            f"Cast: {cast_movie}.")


def increase_rating():
    movies_to_update = Movie.objects.filter(
        is_classic=True,
        rating__lt=10.0,
    )

    if not movies_to_update:
        return "No ratings increased."

    updated_movies = movies_to_update.update(
        rating=F('rating') + 0.1
        )

    return f"Rating increased for {updated_movies} movies."
