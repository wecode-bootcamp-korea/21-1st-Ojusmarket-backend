from django.db import models

from cart.models import Cart

class OrderStatus(models.Model):
    status = models.CharField(max_length=15)

    class Meta:
        db_table = 'orders_statuses'

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    address    = models.CharField(max_length=100)
    status_id  = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    cart_id    = models.ForeignKey(Cart, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'
