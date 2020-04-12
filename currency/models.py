import random

from django.db import models
from django.core.cache import cache

from . import model_choices as mch
from .utils import generate_rate_cache_key


class Rate(models.Model):
    currency = models.PositiveIntegerField(choices=mch.CURRENCY_CHOICES)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.PositiveIntegerField(choices=mch.SOURCE_CHOICES)

    def __str__(self):
        return f'{self.created}/{self.get_currency_display()}/{self.sale}/{self.buy}'

    def save(self, *args, **kwargs):
        if not self.id:
            cache_key = generate_rate_cache_key(self.source, self.currency)
            cache.delete(cache_key)
        super().save(*args, **kwargs)

    @classmethod
    def create_random_rate(cls):
        cls.objects.create(
            currency=random.choice([1, 2]),
            buy=random.randint(20, 30),
            sale=random.randint(20, 30),
            source=random.choice([1, 2]),
        )