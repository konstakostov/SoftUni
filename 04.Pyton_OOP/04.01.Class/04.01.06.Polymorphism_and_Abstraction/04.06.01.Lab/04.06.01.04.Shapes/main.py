from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape, ABC):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return math.pi * self.__radius ** 2

    def calculate_perimeter(self):
        return math.pi * self.__radius * 2


class Rectangle(Shape, ABC):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return self.__height * 2 + self.__width * 2


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

print()

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
