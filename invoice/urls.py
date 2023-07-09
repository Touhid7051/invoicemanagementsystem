from django.urls import path
from .views import InvoiceDetailView


urlpatterns = [
    path('<int:invoice_id>/', InvoiceDetailView.as_view(), name='invoice-detail'),
]
