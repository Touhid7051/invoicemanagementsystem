from django import forms
from .models import Invoice, InvoiceItem


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('invoice_number','customer')

class InvoiceItem(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields =('description', 'quantity', 'price')
        