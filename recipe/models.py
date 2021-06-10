from django.db import models

class RecipeCategory(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'recipes_categories'

class Recipe(models.Model):
    name      = models.CharField(max_length=20)
    category  = models.ForeignKey(RecipeCategory, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=2000)

    class Meta:
        db_table = 'recipes'
