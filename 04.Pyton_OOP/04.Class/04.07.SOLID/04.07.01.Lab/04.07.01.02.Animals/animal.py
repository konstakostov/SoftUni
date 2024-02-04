class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Making sound: "


class Cat(Animal):
    def make_sound(self):
        return super().make_sound() + "meow"


class Chicken(Animal):
    def make_sound(self):
        return super().make_sound() + "cluck"


class Dog(Animal):
    def make_sound(self):
        return super().make_sound() + "woof"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat('Julie'), Dog('Jonny'), Chicken('Mildred')]
animal_sound(animals)
