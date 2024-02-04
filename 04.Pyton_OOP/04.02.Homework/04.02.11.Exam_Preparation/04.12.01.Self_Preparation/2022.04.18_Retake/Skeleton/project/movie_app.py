from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: list = []
        self.users_collection: list = []

    def register_user(self, username: str, age: int):
        user = next(filter(lambda u: u.username == username, self.users_collection), None)

        if user:
            raise Exception("User already exists!")

        new_user = User(username, age)

        self.users_collection.append(new_user)

        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: object):
        user = next(filter(lambda u: u.username == username, self.users_collection), None)

        if not user:
            raise Exception("This user does not exist!")

        if movie not in user.owned_movies:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

    def edit_movie(self, username: str, movie: object, **kwargs):
        pass

    def delete_movie(self, username: str, movie: object):
        pass

    def like_movie(self, username: str, movie: object):
        pass

    def dislike_movie(self, username: str, movie: object):
        pass

    def display_movies(self):
        pass

    def __str__(self):
        pass
