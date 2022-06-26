from django.db import models


class Order(models.Model):
    googl_id = models.IntegerField()
    order_number = models.CharField(max_length=64)
    price_us = models.IntegerField()
    will_arrive = models.DateField()

    def __str__(self):
        return f'Заказ {self.order_number}'
