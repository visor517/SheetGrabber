from django.shortcuts import render
from django.views.generic import ListView

from .models import Order
from .utils import get_sheet


class OrdersListView(ListView):
    model = Order
    template_name = 'index.html'

    def get_queryset(self):
        get_sheet()
        return Order.objects.all()
