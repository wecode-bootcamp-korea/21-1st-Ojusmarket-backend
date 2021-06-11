import json

from django.views import View
from django.http import JsonResponse

from ingredient.models import Ingredient, IngredientMainCategory
from recipe.models import Recipe

class MaincategoryView(View):
    def get(self, request):

        ingredient_results = Ingredient.objects.all()

    
        result = []

        for ingredient_result in ingredient_results:
            result.append({
                'id'          : ingredient_result.id,
                'name'        : ingredient_result.name,
                'price'       : ingredient_result.price,
                'storage'     : ingredient_result.storage,
                'category_id' : ingredient_result.category.main_category_id,
                'image_url'   : ingredient_result.image_url
            })

        recipe_results = Recipe.objects.all()

        recipes_result = []

        for recipe_result in recipe_results:
            recipes_result.append({
                'id'          : recipe_result.id,
                'name'        : recipe_result.name,
                'image_url'   : recipe_result.image_url,
                'category_id' : recipe_result.category_id
            })

        return JsonResponse({'ingredient':result, 'recipe': recipes_result}, status=200)