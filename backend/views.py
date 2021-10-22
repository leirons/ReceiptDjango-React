from rest_framework import generics
from . import serializers
from .models import Receipt
from rest_framework.decorators import api_view
from django.http.response import HttpResponse

class Receipts(generics.ListCreateAPIView):
    queryset = Receipt.objects.all()
    serializer_class = serializers.ReceiptSerializer
