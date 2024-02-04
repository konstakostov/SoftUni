from django.db import models
from django.db.models import Count


class DirectorManager(models.Manager):
    def get_directors_by_movies_count(self):
        return self.annotate(
            movies_made=Count('movies_directed'),
        ).order_by(
            '-movies_made',
            'full_name',
        )

