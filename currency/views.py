import csv
from django.views.generic import ListView, View
from django.http import HttpResponse

from .models import Rate


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
