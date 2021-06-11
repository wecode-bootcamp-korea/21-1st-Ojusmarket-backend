import os, django, csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ojusmarket.settings")
django.setup()

from ingredient.models import IngredientMainCategory, IngredientSubCategory, IngredientRecipe, Ingredient
from recipe.models import RecipeCategory, Recipe

CSV_PATH_INGREDIENTMAINCATEGORY = './ingredient_main_category.csv'
CSV_PATH_INGREDIENTSUBCATEGORY = './ingredient_sub_category.csv'
CSV_PATH_INGREDIENTS = './ingredients.csv'
CSV_PATH_RECIPECATEGORY = './recipe_category.csv'
CSV_PATH_RECIPES = './recipe.csv'
CSV_PATH_INGREDIENTRECIPE = './ingredients_recipes.csv'

IngredientMainCategory.objects.all().delete()
IngredientSubCategory.objects.all().delete()
IngredientRecipe.objects.all().delete()
Ingredient.objects.all().delete()
Recipe.objects.all().delete()
RecipeCategory.objects.all().delete()

with open(CSV_PATH_INGREDIENTMAINCATEGORY, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        IngredientMainCategory.objects.create(**row)

with open(CSV_PATH_INGREDIENTSUBCATEGORY, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        IngredientSubCategory.objects.create(**row)

with open(CSV_PATH_RECIPECATEGORY, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        RecipeCategory.objects.create(**row)

with open(CSV_PATH_RECIPES, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Recipe.objects.create(**row)

with open(CSV_PATH_INGREDIENTS, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Ingredient.objects.create(**row)

with open(CSV_PATH_INGREDIENTRECIPE, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        IngredientRecipe.objects.create(**row)

