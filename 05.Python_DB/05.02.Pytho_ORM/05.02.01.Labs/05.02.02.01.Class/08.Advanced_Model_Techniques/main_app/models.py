from django.core import validators
from django.db import models
from main_app.validators import validate_menu_categories


# Create your models here.
class Restaurant(models.Model):
    # name = models.CharField(
    #     max_length=100,
    #     validators=[
    #         validators.MinLengthValidator(
    #             2,
    #             "Name must be at least 2 characters long."
    #         )
    #     ],
    #     validators=[
    #         validators.MaxLengthValidator(
    #             2,
    #             "Name cannot exceed 100 characters."
    #         )
    #     ],
    #
    #     ]
    # )

    name = models.CharField(
        max_length=100,
        validators=[
            validators.MinLengthValidator(
                2,
                "Name must be at least 2 characters long."
            ),
            validators.MaxLengthValidator(
                100,
                "Name cannot exceed 100 characters."
            )
        ]
    )

    location = models.CharField(
        max_length=200,
        validators=[
            validators.MinLengthValidator(
                2,
                "Location must be at least 2 characters long.",
            ),
            validators.MaxLengthValidator(
                200,
                "Location cannot exceed 200 characters."
            )
        ]
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[
            validators.MinValueValidator(
                0,
                "Rating must be at least 0.00."
            ),
            validators.MaxValueValidator(
            5,
                "Rating cannot exceed 5.00."
            )
        ]
    )


class Menu(models.Model):
    name = models.CharField(
        max_length=100,
    )

    description = models.TextField(
        validators=[validate_menu_categories]
    )

    restaurant = models.ForeignKey(
        to=Restaurant,
        on_delete=models.CASCADE,
    )


class RestaurantReview(models.Model):
    reviewer_name = models.CharField(
        max_length=100,
    )

    restaurant = models.ForeignKey(
        to=Restaurant,
        on_delete=models.CASCADE,
    )

    review_content = models.TextField()

    rating = models.PositiveIntegerField(
        validators=[
            validators.MaxValueValidator(5),
        ]
    )

    class Meta:
        ordering = ['-rating']
        verbose_name = "Restaurant Review"
        verbose_name_plural = "Restaurant Reviews"
        unique_together = ('reviewer_name', 'restaurant')

        abstract = True


class RegularRestaurantReview(RestaurantReview):
    pass


class FoodCriticRestaurantReview(RestaurantReview):
    food_critic_cuisine_area = models.CharField(
        max_length=100,
    )

    class Meta:
        verbose_name = "Food Critic Review"
        verbose_name_plural = "Food Critic Reviews"


class MenuReview(models.Model):
    reviewer_name = models.CharField(
        max_length=100,
    )

    menu = models.ForeignKey(
        to=Menu,
        on_delete=models.CASCADE,
    )

    review_content = models.TextField()

    rating = models.PositiveIntegerField(
        validators=[
            validators.MaxValueValidator(5)
        ]
    )

    class Meta:
        ordering = ['-rating']
        verbose_name = "Menu Review"
        verbose_name_plural = "Menu Reviews"
        unique_together = ['reviewer_name', 'menu']
        indexes = [
            models.Index(
                fields=["menu"],
                name="main_app_menu_review_menu_id"
            )
        ]


class ReviewMixin(models.Model):
    ra


