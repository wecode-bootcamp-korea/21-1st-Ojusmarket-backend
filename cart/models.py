from django.db.models.deletion import CASCADE
from django.db import models

from ingredient.models import Ingredient
from user.models import User

class Cart(models.Model):
    count         = models.IntegerField()
    user_id       = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    class Meta:
        db_table = 'carts'