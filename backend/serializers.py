from rest_framework import serializers

from .models import Receipt


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model: Receipt = Receipt
        fields:list = ['image','name','description','created_at','is_moderated']
