from django.db import models


class Order(models.Model):
    google_id = models.IntegerField(null=True)
    order_number = models.CharField(max_length=64, null=True)
    price_us = models.FloatField(null=True)
    price_ru = models.FloatField(null=True)
    will_arrive = models.DateField(null=True)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return f'Заказ {self.order_number}'
