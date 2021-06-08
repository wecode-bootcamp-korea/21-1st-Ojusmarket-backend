from django.db import models



class CategoryRecipe(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'categories_recipes'

class Recipe(models.Model):
    name     = models.CharField(max_length=20)
    category = models.ForeignKey(CategoryRecipe, on_delete=models.CASCADE)
    image    = models.TextField()

    class Meta:
        db_table = 'recipes'
