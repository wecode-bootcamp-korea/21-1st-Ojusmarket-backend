from django.db import models

from ingredient.models import Ingredient
from user.models import User

class Like(models.Model):
    created_at   = models.DateTimeField(auto_now_add=True)
    user         = models.ForeignKey(User, on_delete=models.CASCADE,related_name='like_user')
    ingredient   = models.ForeignKey(Ingredient, on_delete=models.CASCADE,related_name='like_ingredient')
<<<<<<< HEAD
    false_delete = models.BooleanField(default=False)

=======
    false_delete = models.BooleanField(default=False) 
    
>>>>>>> main
    class Meta:
        db_table = 'likes'