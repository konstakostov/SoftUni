from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Pet(models.Model):
    name = models.CharField(
        max_length=30,
    )

    personal_pet_photo = models.URLField()

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        null=True,      # Can be null value
        blank=True,     # Can be left blank
        unique=True,    # Must be unique
        editable=False, # Can't be edited
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")

        super().save(*args, **kwargs)
