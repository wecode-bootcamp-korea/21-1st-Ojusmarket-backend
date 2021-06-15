import json
from user.models import User

from django.views import View
from django.http import JsonResponse

from ingredient.models import Ingredient

class IngredientsView(View):
    def get(self, request):

        category_id = request.GET.get('category_id', None)
        if category_id == None:

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