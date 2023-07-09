from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Invoice, InvoiceItem
from .serializers import InvoiceSerializer, InvoiceItemSerializer


# Create your views here.

class InvoiceDetailView(APIView):
    def get(self, request, invoice_id):
        try:
            invoice = Invoice.objects.get(id=invoice_id)
            serializer = InvoiceSerializer(invoice)
            return Response(serializer.data)
        except Invoice.DoesNotExist:
            return Response({'message': 'Invoice not found'}, status=404)