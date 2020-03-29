import json
from django.db import models
from django.http import JsonResponse
import django_filters

from rest_framework import generics, filters, viewsets

from currency.models import Rate
from .serializers import RateSerializer


class RatesView(generics.ListCreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class RateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class RatesSourceView(generics.ListAPIView):
    serializer_class = RateSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        source_pk = self.kwargs['source_pk']
        return Rate.objects.filter(source=source_pk)

class RatesCurrencyView(generics.ListAPIView):
    serializer_class = RateSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        currency_pk = self.kwargs['currency_pk']
        return Rate.objects.filter(currency=currency_pk)


class CreatedFilter(filters.FilterSet):
    class Meta:
        model = Rate
        fields = {
            'created': ('exact', 'lt', 'gt', 'lte', 'gte')
        }

    filter_overrides = {
        models.DateTimeField: {
            'filter_class': django_filters.IsoDateTimeFilter
        },
    }


class CreatedFilterView(viewsets.ReadOnlyModelViewSet):
    filter_class = CreatedFilter