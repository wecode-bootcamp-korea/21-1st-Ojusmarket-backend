from django.db import models

from user.models import User
from ingredient.models import Ingredient

class Like(models.Model):
    date       = models.DateField()
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    class Meta:
        db_table = 'likes'