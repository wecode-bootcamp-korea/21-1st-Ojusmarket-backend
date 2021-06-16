<<<<<<< HEAD
=======

>>>>>>> b0748562f247fb1c79dcca6a331dd4032bc5bcfa
import os, django, csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ojusmarket.settings")
django.setup()

from ingredient.models import IngredientMainCategory, IngredientSubCategory, IngredientRecipe, Ingredient
from recipe.models import RecipeCategory, Recipe
<<<<<<< HEAD
=======
from order.models import OrderStatus
>>>>>>> b0748562f247fb1c79dcca6a331dd4032bc5bcfa

CSV_PATH_INGREDIENTMAINCATEGORY = './ingredient_main_category.csv'
CSV_PATH_INGREDIENTSUBCATEGORY = './ingredient_sub_category.csv'
CSV_PATH_INGREDIENTS = './ingredients.csv'
CSV_PATH_RECIPECATEGORY = './recipe_category.csv'
CSV_PATH_RECIPES = './recipe.csv'
<<<<<<< HEAD
CSV_PATH_INGREDIENTRECIPE = './ojus - ingredients_recipes.csv'
=======
CSV_PATH_INGREDIENTRECIPE = './ingredients_recipes.csv'
CSV_PATH_ORDERSTATUS = './order_status.csv'
>>>>>>> b0748562f247fb1c79dcca6a331dd4032bc5bcfa

IngredientMainCategory.objects.all().delete()
IngredientSubCategory.objects.all().delete()
IngredientRecipe.objects.all().delete()
Ingredient.objects.all().delete()
Recipe.objects.all().delete()
RecipeCategory.objects.all().delete()
<<<<<<< HEAD
=======
OrderStatus.objects.all().delete()
>>>>>>> b0748562f247fb1c79dcca6a331dd4032bc5bcfa

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

<<<<<<< HEAD
=======
with open(CSV_PATH_ORDERSTATUS, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        OrderStatus.objects.create(**row)
>>>>>>> b0748562f247fb1c79dcca6a331dd4032bc5bcfa
