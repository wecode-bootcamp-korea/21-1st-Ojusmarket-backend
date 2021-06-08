from django.db import models
from django.db.models.deletion import CASCADE

from recipe.models import Recipe
from user.models import User

class MainCategoryIngredient(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'main_categories_ingredients'

class SubCategoryIngredient(models.Model):
    name = models.CharField(max_length=10)
    main = models.ForeignKey(MainCategoryIngredient, on_delete=models.CASCADE)

    class Meta:
        db_table = 'sub_categories_ingredients'

class Ingredient(models.Model):
    name     = models.CharField(max_length=50)
    image    = models.TextField()
    price    = models.DecimalField(max_digits=18, decimal_places=2)
    storage  = models.CharField(max_length=10)
    info     = models.CharField(max_length=50)
    category = models.ForeignKey(SubCategoryIngredient, on_delete=models.CASCADE)
    recipe   = models.ManyToManyField(Recipe, through='IngredientRecipe')
    user     = models.ManyToManyField(User)

    class Meta:
        db_table = 'ingredients'

class IngredientRecipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe     = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ingredients_recipes'
