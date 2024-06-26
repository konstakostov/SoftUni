from django.db import models
from django.db.models import Count


class ProfileManager(models.Manager):
    def get_regular_customers(self):
        return self.annotate(
            total_orders=Count('order')
        ).filter(
            total_orders__gt=2,
        ).order_by(
            '-total_orders'
        )
