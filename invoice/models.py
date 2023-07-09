from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    # Add other customer fields as needed

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # Add other invoice fields as needed

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    description = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)