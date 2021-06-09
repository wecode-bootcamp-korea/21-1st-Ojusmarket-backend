from django.db import models
from django.db.models.deletion import CASCADE

from recipe.models import Recipe
from user.models import User

class MainCategoryIngredient(models.Model):
    name       = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'main_categories_ingredients'

class IngredientSubCategory(models.Model):
    name             = models.CharField(max_length=10)
    main_category_id = models.ForeignKey(MainCategoryIngredient, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ingredient_sub_categories'

class Ingredient(models.Model):
    name        = models.CharField(max_length=50)
    image_url   = models.CharField(max_length=2000)
    price       = models.DecimalField(max_digits=18, decimal_places=2)
    storage     = models.CharField(max_length=10)
    info        = models.CharField(max_length=50)
    category_id = models.ForeignKey(IngredientSubCategory, on_delete=models.CASCADE)
    recipe_id   = models.ManyToManyField(Recipe, through='IngredientRecipe')
    user_id     = models.ManyToManyField(User, through='like.Like')

    class Meta:
        db_table = 'ingredients'

class IngredientRecipe(models.Model):
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe_id     = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ingredients_recipes'
