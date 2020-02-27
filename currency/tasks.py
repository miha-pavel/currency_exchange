from decimal import Decimal

import requests
from celery import shared_task
from bs4 import BeautifulSoup

from currency.models import Rate
from currency import model_choices as mch


def get_soup(url):
    response = requests.get(url)
    html = response.text
    return BeautifulSoup(html, 'html.parser')


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
def _vkurse():
    url = 'http://vkurse.dp.ua/course.json'
    response = requests.get(url)
    for key, rate in response.json().items():
        if key in {'Dollar', 'Euro'}:
            currency = {
                'Dollar': mch.CURR_USD,
                'Euro': mch.CURR_EUR,
            }[key]
            rate_kwargs = {
                'currency': currency,
                'buy': Decimal(rate['buy']),
                'sale': Decimal(rate['sale']),
                'source': mch.SR_VKURSE,
            }
            new_rate = Rate(**rate_kwargs)
            last_rate = Rate.objects.filter(
                currency=currency,
                source=mch.SR_VKURSE
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
def _ukrsib():
    url = 'https://my.ukrsibbank.com/ua/personal/operations/currency_exchange/'
    soup = get_soup(url)
    exchange_rate = soup.findAll("table", {"class": "currency__table"})
    table_body = exchange_rate[0].find('tbody')
    rows = table_body.findAll('tr')
    data = []
    for row in rows:
        cols = row.findAll('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    print('data: ', data)
    for item in data:
        print(item)


@shared_task()
def _otp_bank():
    url = 'https://www.otpbank.com.ua/local/components/otp/utils.exchange_rate_arc/exchange_rate_by_date.php?ib_code=otp_bank_currency_rates'
    response = requests.get(url)
    for rate in response.json()['items']:
        if rate['NAME'] in {'USD', 'EUR'}:
            currency = {
                'USD': mch.CURR_USD,
                'EUR': mch.CURR_EUR,
            }[rate['NAME']]
            rate_kwargs = {
                'currency': currency,
                'buy': Decimal(rate['BUY']),
                'sale': Decimal(rate['SELL']),
                'source': mch.SR_OTP,
            }
            new_rate = Rate(**rate_kwargs)
            last_rate = Rate.objects.filter(
                currency=currency,
                source=mch.SR_OTP
                ).last()
            if last_rate is None or (new_rate.buy != last_rate.buy or new_rate.sale != last_rate.sale):
                new_rate.save()


@shared_task()
def _tascom_bank():
    url = 'https://tascombank.ua/api/currencies'
    response = requests.get(url)
    list_exchanges = [exch for exch in response.json()[0] if exch.get('kurs_type') == 'exchange']
    for rate in list_exchanges:
        if rate['short_name'] in {'USD', 'EUR'}:
            currency = {
                'USD': mch.CURR_USD,
                'EUR': mch.CURR_EUR,
            }[rate['short_name']]
            rate_kwargs = {
                'currency': currency,
                'buy': Decimal(rate['kurs_buy']),
                'sale': Decimal(rate['kurs_sale']),
                'source': mch.SR_TAS,
            }
            new_rate = Rate(**rate_kwargs)
            last_rate = Rate.objects.filter(
                currency=currency,
                source=mch.SR_TAS
                ).last()
            if last_rate is None or (new_rate.buy != last_rate.buy or new_rate.sale != last_rate.sale):
                new_rate.save()


@shared_task()
def parse_rates():
    _privat.delay()
    _mono.delay()
    _vkurse.delay()
    _otp_bank.delay()
    _tascom_bank.delay()
