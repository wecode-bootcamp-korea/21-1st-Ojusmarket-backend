import json
from user.models import User

from django.views import View
from django.http import JsonResponse

from ingredient.models import Ingredient

class IngredientcategoriesView(View):
    def get(self, request):
    
        category_id = request.GET['category_id']

        ingredient_results = Ingredient.objects.filter(category_id = category_id)

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

        return JsonResponse({'ingredients' : result}, status=200)

class IngredientsView(View):
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

        return JsonResponse({'ingredients' : result}, status=200)