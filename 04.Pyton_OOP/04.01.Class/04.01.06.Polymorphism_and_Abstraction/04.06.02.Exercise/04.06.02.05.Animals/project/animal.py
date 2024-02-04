from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def make_sound(self) -> str:
        ...

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} " \
               f"year old {self.gender} {self.__class__.__name__}"



