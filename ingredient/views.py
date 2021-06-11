import json

from django.views import View
from django.http import JsonResponse

from ingredient.models import Ingredient, IngredientSubCategory
from recipe.models import Recipe

class MaincategoryView(View):
    def get(self, request):

        ingredient_result = Ingredient.objects.all()

        ingredients_result = []

        for ingredient_results in ingredient_result:
            ingredients_result.append({
                'id'          : ingredient_results.id,
                'name'        : ingredient_results.name,
                'price'       : ingredient_results.price,
                'storage'     : ingredient_results.storage,
                'category_id' : ingredient_results.category_id,
                'image_url'   : ingredient_results.image_url,
            })

        recipe_result = Recipe.objects.all()

        recipes_result = []

        for recipe_results in recipe_result:
            recipes_result.append({
                'id'          : recipe_results.id,
                'name'        : recipe_results.name,
                'image_url'   : recipe_results.image_url,
                'category_id' : recipe_results.category_id
            })

        return JsonResponse({'ingredient':ingredients_result, 'recipe': recipes_result}, status=200)