from django.db import models

from recipe.models import Recipe
from user.models import User

class IngredientMainCategory(models.Model):
    name       = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ingredients_main_categories'

class IngredientSubCategory(models.Model):
    name          = models.CharField(max_length=10)
    main_category = models.ForeignKey(IngredientMainCategory, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ingredients_sub_categories'

class Ingredient(models.Model):
    name      = models.CharField(max_length=50)
    image_url = models.CharField(max_length=2000)
    price     = models.DecimalField(max_digits=18, decimal_places=2)
    storage   = models.CharField(max_length=10)
    info      = models.CharField(max_length=50)
    category  = models.ForeignKey(IngredientSubCategory, on_delete=models.CASCADE)
    recipe    = models.ManyToManyField(Recipe, through='IngredientRecipe')
    user      = models.ManyToManyField(User, through='like.Like')

    class Meta:
        db_table = 'ingredients'

class IngredientRecipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe     = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ingredients_recipes'
