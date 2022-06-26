from django.shortcuts import render
from django.views.generic import ListView

from .models import Order


class OrdersListView(ListView):
    model = Order
    template_name = 'index.html'
