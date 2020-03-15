from django.core.management.base import BaseCommand

from currency.tasks import _privat_4_years


class Command(BaseCommand):
    help = 'Get currency rate for 4 years from privatbank'

    def handle(self, *args, **options):
        _privat_4_years.delay()
