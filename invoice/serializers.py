from rest_framework import serializers
from .models import InvoiceItem ,Invoice


class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ('description', 'quantity', 'price')

class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ('invoice_number', 'customer', 'items')