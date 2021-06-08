from django.db import models

from cart.models import Cart

class OrderStatus(models.Model):
    status = models.CharField(max_length=15)

    class Meta:
        db_table = 'order_statuses'

class Order(models.Model):
    date    = models.DateField()
    address = models.CharField(max_length=100)
    status  = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    cart    = models.ForeignKey(Cart, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'
