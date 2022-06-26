from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Order


class OrderModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
