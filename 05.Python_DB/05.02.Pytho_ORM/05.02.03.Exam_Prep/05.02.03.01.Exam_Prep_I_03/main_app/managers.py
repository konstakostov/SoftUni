from django.db import models
from django.db.models import Count


class DirectorManager(models.Manager):
    def get_directors_by_movies_count(self):
        return self.annotate(
            total_movies_count=Count('movies_directed'),
        ).order_by(
            '-total_movies_count',
            'full_name',
        )
