from django.db import models

from cart.models import Cart

class OrderStatus(models.Model):
    status = models.CharField(max_length=16)

    class Meta:
        db_table = 'order_status'

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    address    = models.CharField(max_length=100)
    status     = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    cart       = models.ForeignKey(Cart, on_delete=models.CASCADE)
    class Meta:
        db_table = 'orders'