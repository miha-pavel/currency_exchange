from django.db import models

from . import model_choices as mch


class Rate(models.Model):
    currency = models.PositiveIntegerField(choices=mch.CURRENCY_CHOICES)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.PositiveIntegerField(choices=mch.SOURCE_CHOICES)

    def __str__(self):
        return f'{self.created}/{self.get_currency_display()}/{self.sale}/{self.buy}'
