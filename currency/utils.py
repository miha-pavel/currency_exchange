import hashlib

# from .models import Rate


# def save_rate_data(source, rate_kwargs):
#     new_rate = Rate(**rate_kwargs)
#     last_rate = Rate.objects.filter(
#         currency=rate_kwargs['currency'],
#         source=source,
#         ).last()
#     if last_rate is None or (new_rate.buy != last_rate.buy or new_rate.sale != last_rate.sale):
#         new_rate.save()

def generate_rate_cache_key(source: int, currency: int) -> str:
    key = f'latest-rates-{source}-{currency}'.encode()
    return hashlib.md5(key).hexdigest()