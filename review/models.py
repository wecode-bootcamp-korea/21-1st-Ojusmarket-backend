from django.db import models

from user.models       import User
from ingredient.models import Ingredient

class Review(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000) 
    created_at = models.DateField(auto_now_add=True)
 
    class Meta:
        db_table = 'reviews'