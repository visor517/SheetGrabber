from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.viewsets import ModelViewSet

from .models import Order
from .serializers import OrderModelSerializer


class OrdersListView(ListView):
    model = Order
    template_name = 'index.html'


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
