from django.db.models.deletion import CASCADE
from django.db import models

from ingredient.models import Ingredient
from user.models import User

class Cart(models.Model):
    count       = models.IntegerField()
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredient  = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    soft_delete = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'carts'