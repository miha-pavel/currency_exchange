import csv

from django.views.generic import ListView, View, TemplateView
from django.http import HttpResponse
from django.core.cache import cache

from .models import Rate
from . import model_choices as mch
from .utils import generate_rate_cache_key


class RateList(ListView):
    model = Rate
    paginate_by = 5
    queryset = Rate.objects.all()[:20]


class RateCSV(View):
    HEADERS = ['id', 'created', 'currency', 'buy', 'sale', 'source']

    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content_Disposition'] = 'attachment; filename="rates.csv"'
        writer = csv.writer(response)
        
        writer.writerow(self.HEADERS)
        for rate in Rate.objects.all().iterator():
            row = [
                getattr(rate, f'get_{attr}_display')()
                if hasattr(rate, f'get_{attr}_display') else getattr(rate, attr)
                for attr in self.HEADERS
                ]
            writer.writerow(row)
        #     writer.writerow(map(str, [
        #         rate.id,
        #         rate.created,
        #         rate.get_currency_display(),
        #         rate.buy,
        #         rate.sale,
        #         rate.get_source_display()
        #     ]))
        return response


class LatestRate(TemplateView):
    template_name = "latest_rates.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rates = []
        for bank in mch.SOURCE_CHOICES:
            source = bank[0]
            for curr in mch.CURRENCY_CHOICES:
                currency = curr[0]
                cache_key = generate_rate_cache_key(source, currency)
                #DB
                rate = cache.get(cache_key)
                if rate is None:
                    rate = Rate.objects.filter(source=source, currency=currency).order_by('created').last()
                    if rate:
                        rate_dict = {
                            'currency': rate.currency,
                            'source': rate.source,
                            'sale': rate.sale,
                            'buy': rate.buy,
                            'created': rate.created,
                        }
                        rates.append(rate_dict)
                        cache.set(cache_key, rate_dict, 60*15)
                else:
                    rates.append(rate)
        context["rates"] = rates
        return context
