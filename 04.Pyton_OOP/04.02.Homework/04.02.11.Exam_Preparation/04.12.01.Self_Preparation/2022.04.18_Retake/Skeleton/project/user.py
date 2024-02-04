class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age

        self.movies_liked: list = []
        self.movies_owned: list = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value.strip() == "":
            raise ValueError("Invalid username!")

        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")

        self.__age = value

    def __str__(self):
        result = f"Username: {self.username}, Age: {self.age}\n"

        result += "Liked movies:\n"
        if len(self.movies_liked) == 0:
            result += "No movies liked.\n"
        else:
            for movie in self.movies_liked:
                result += f"{movie.details()}\n"

        result += "Owned movies:\n"
        if len(self.movies_owned) == 0:
            result += "No movies owned.\n"
        else:
            for movie in self.movies_owned:
                result += f"{movie.details()}\n"
