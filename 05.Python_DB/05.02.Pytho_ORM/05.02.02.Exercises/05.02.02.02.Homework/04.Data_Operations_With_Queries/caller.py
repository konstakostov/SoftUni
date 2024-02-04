import os
from decimal import Decimal

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


# Create queries within functions
def create_pet(name: str, species: str):
    Pet.objects.create(
        name=name,
        species=species,
    )

    return f"{name} is a very cute {species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    new_artifact = Artifact(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )

    new_artifact.save()

    return f"The artifact {name} is {age} years old!"


def delete_all_artifacts():
    all_artifacts = Artifact.objects.all()

    all_artifacts.delete()


def show_all_locations():
    all_locations = Location.objects.all().order_by("-id")

    result = []

    for location in all_locations:
        result.append(f"{location.name} has a population of {location.population}!")

    return '\n'.join(result)


def new_capital():
    capital = Location.objects.first()

    capital.is_capital = True
    capital.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values("name")


def delete_first_location():
    Location.objects.first().delete()


def apply_discount():
    cars = Car.objects.all()

    for car in cars:
        percent_off = Decimal(sum(int(x) for x in str(car.year)) / 100)
        discount = Decimal(car.price) * percent_off

        car.price_with_discount = car.price - discount

        car.save()


def get_recent_cars():
    return Car.objects.filter(year__gte=2020).values('model', 'price_with_discount')


def delete_last_car():
    Car.objects.last().delete()


def show_unfinished_tasks():
    tasks = Task.objects.filter(is_finished=False)

    result = []

    for task in tasks:
        result.append(f"Task - {task.title} needs to be done until {task.due_date}!")

    return '\n'.join(result)


def complete_odd_tasks():
    tasks = Task.objects.all()

    for task in tasks:
        if task.id % 2 != 0:
            task.is_finished = True

            task.save()


def encode_and_replace(text: str, task_title: str):
    new_title = ""
    for char in text:
        new_title += chr(ord(char) - 3)

    chosen_ask = Task.objects.filter(title=task_title).first()
    chosen_ask.title = new_title


def get_deluxe_rooms():
    rooms = HotelRoom.objects.filter(room_type="Deluxe")

    result = []

    for room in rooms:
        result.append(f"Deluxe room with number {room.room_number} costs {room.price_per_night}$ per night!")

    return '\n'.join(result)


def increase_room_capacity():
    rooms = HotelRoom.objects.order_by("id")

    previous_room_capacity = None

    for room in rooms:
        if not room.is_reserved:
            continue

        if previous_room_capacity:
            room.capacity += previous_room_capacity
        else:
            room.capacity += room.id

        previous_room_capacity = room.capacity

        room.save()


def reserve_first_room():
    room = HotelRoom.objects.first()
    room.is_reserved = True

    room.save()


def delete_last_room():
    room = HotelRoom.objects.last()
    if room.is_reserved:
        room.delete()


def update_characters():
    characters = Character.objects.all()

    for character in characters:
        if character.class_name == "Mage":
            character.level += 3
            character.intelligence -= 7

        elif character.class_name == "Warrior":
            character.hit_points -= character.hit_points / 2
            character.dexterity += 4

        elif character.class_name == "Assassin" or character.class_name == "Scout":
            character.inventory = "The inventory is empty"

        character.save()


def fuse_characters(first_character, second_character):
    new_inventory = None
    if first_character.class_name == "Mage" or first_character.class_name == "Scout":
        new_inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    elif second_character.class_name == "Warrior" or second_character.class_name == "Assassin":
        new_inventory = "Dragon Scale Armor, Excalibur"

    new_character = Character(
        name=f"{first_character.name} {second_character.name}",
        class_name="Fusion",
        level=round((first_character.level + second_character.level) // 2),
        strength=round((first_character.strength + second_character.strength) * 1.2),
        dexterity=round((first_character.dexterity + second_character.dexterity) * 1.4),
        intelligence=round((first_character.intelligence + second_character.intelligence) * 1.5),
        hit_points=round((first_character.hit_points + second_character.hit_points)),
        inventory=new_inventory
    )

    new_character.save()


def grand_dexterity():
    characters = Character.objects.all()

    for character in characters:
        character.dexterity = 30

        character.save()


def grand_intelligence():
    characters = Character.objects.all()

    for character in characters:
        character.intelligence = 40

        character.save()


def grand_strength():
    characters = Character.objects.all()

    for character in characters:
        character.strength = 50

        character.save()


def delete_characters():
    characters = Character.objects.filter(
        inventory="The inventory is empty"
    )

    for character in characters:
        character.delete()

