import json

from django.http import JsonResponse

from rest_framework import generics

from currency.models import Rate
from .serializers import RateSerializer


def hello_world(request):
    return JsonResponse({'hello': 'world'})
# http://localhost:8000/api/v1/currency/rates/


class RatesView(generics.ListCreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class RateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
