from django.db import models

from ingredient.models import Ingredient
from user.models import User

class Like(models.Model):
    created_at    = models.DateTimeField(auto_now_add=True)
    user_id       = models.ForeignKey(User, on_delete=models.CASCADE,related_name='like_user')
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE,related_name='like_ingredient')

    class Meta:
        db_table = 'likes'