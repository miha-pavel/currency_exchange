import requests
from decimal import Decimal

from celery import shared_task, task

from .models import Rate
from . import model_choices as mch


@shared_task()
def _privat():
    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    response = requests.get(url)
    print('response:---------------', response)
    for rate in response.json:
        if rate['ccy'] in {'USD', 'EUR'}:
            currency = {
                'USD': mch.CURR_USD,
                'EUR': mch.CURR_EUR,
            }[rate['ccy']]
            rate_kwargs = {
                'currency': currency,
                'buy': Decimal(rate['buy']),
                'sale': Decimal(rate['sale']),
                'source': mch.SR_PRIVAT,
            }
            new_rate = Rate(**rate_kwargs)
            last_rate = Rate.objects.filter(
                currency=currency,
                source=mch.SR_PRIVAT
                ).last()
            if last_rate is None\
                or (new_rate.buy != last_rate.buy or new_rate.sale != last_rate.sale):
                new_rate.save()
            Rate.objects.create(**rate_kwargs)


@shared_task()
def parse_rates():
    _privat().delay()
