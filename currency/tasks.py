from decimal import Decimal

import requests
from celery import shared_task

from currency.models import Rate
from currency import model_choices as mch


@shared_task()
def _privat():
    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    response = requests.get(url)
    for rate in response.json():
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
            if last_rate is None or (new_rate.buy != last_rate.buy or new_rate.sale != last_rate.sale):
                new_rate.save()


@shared_task()
def _mono():
    url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(url)
    for index, rate in enumerate(response.json()[:2]):
        currency = index+1
        rate_kwargs = {
            'currency': currency,
            'sale': rate.get("rateSell"),
            'buy': rate.get("rateBuy"),
            'source': mch.SR_MONO,
        }
        new_rate = Rate(**rate_kwargs)
        last_rate = Rate.objects.filter(
            currency=currency,
            source=mch.SR_MONO
            ).last()
        if last_rate is None or (new_rate.buy != last_rate.buy or new_rate.sale != last_rate.sale):
            new_rate.save()

@shared_task()
def parse_rates():
    _privat()
    _mono()
