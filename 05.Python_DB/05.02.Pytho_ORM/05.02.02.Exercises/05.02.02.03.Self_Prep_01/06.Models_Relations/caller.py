import os
from datetime import timedelta, date

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import (
    Author, Book,
    Artist, Song,
    Product, Review,
    Driver, DrivingLicense,
    Owner, Registration, Car,
    )


# Create queries within functions
def show_all_authors_with_their_books() -> str:
    result = []

    authors = Author.objects.all().order_by('id')

    for author in authors:
        books = Book.objects.filter(author=author)

        if not books:
            continue

        titles = ', '.join(b.title for b in books)

        result.append(f"{author.name} has written - {titles}")

    return '\n'.join(result)


def delete_all_authors_without_books() -> None:
    Author.objects.filter(book__isnull=True).delete()


def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    new_song = Song.objects.get(title=song_title)

    artist.songs.add(new_song)


def get_songs_by_artist(artist_name: str):
    artist = Artist.objects.get(name=artist_name)

    return artist.songs.all().order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song_to_remove = Song.objects.get(title=song_title)

    artist.songs.remove(song_to_remove)


def calculate_average_rating_for_product_by_name(product_name: str):
    product = Product.objects.get(name=product_name)
    reviews = product.reviews.all()

    rating_sum = sum(r.rating for r in reviews)
    average_rating = rating_sum / len(reviews)

    return average_rating


def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews():
    Product.objects.filter(reviews__isnull=True).delete()


def calculate_licenses_expiration_dates():
    licenses = DrivingLicense.objects.order_by('-license_number')

    return '\n'.join(str(l) for l in licenses)


def get_drivers_with_expired_licenses(due_date):
    license_issue_date = due_date - timedelta(days=365)

    expired = Driver.objects.filter(
        drivinglicense__issue_date__gt=license_issue_date
    )

    return expired


def register_car_by_owner(owner):
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(
        registration__isnull=True,
        owner=owner
    ).first()

    car.owner = owner
    car.registration = registration

    car.save()

    registration.registration_date = date.today()
    registration.car = car

    registration.save()

    return (f"Successfully registered {car.model} to {owner.name} with "
            f"registration number {registration.registration_number}.")


































































































































































