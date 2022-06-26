from django.db import models


class Order(models.Model):
    google_id = models.IntegerField(null=True)
    order_number = models.CharField(max_length=64)
    price_us = models.IntegerField(null=True)
    price_ru = models.IntegerField(null=True)
    will_arrive = models.DateField(null=True)

    def __str__(self):
        return f'Заказ {self.order_number}'
