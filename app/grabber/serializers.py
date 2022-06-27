from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Order


class OrderModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['google_id', 'order_number', 'price_us', 'price_ru', 'will_arrive', 'is_valid']
