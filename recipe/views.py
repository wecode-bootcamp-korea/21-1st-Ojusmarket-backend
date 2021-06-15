import json

from django.views import View
from django.http import JsonResponse

from recipe.models import Recipe

class RecipesView(View):
    def get(self, request):

        category_id = request.GET.get('category_id', None)
        if category_id == None:

            recipe_results = Recipe.objects.all()

            recipes_result = []

            for recipe_result in recipe_results:
                recipes_result.append({
                    'id'          : recipe_result.id,
                    'name'        : recipe_result.name,
                    'image_url'   : recipe_result.image_url,
                    'category_id' : recipe_result.category_id
                })

            return JsonResponse({'recipe': recipes_result}, status=200)

        recipe_results = Recipe.objects.filter(category_id = category_id)

        recipes_result = []

        for recipe_result in recipe_results:
            recipes_result.append({
                'id'          : recipe_result.id,
                'name'        : recipe_result.name,
                'image_url'   : recipe_result.image_url,
                'category_id' : recipe_result.category_id
            })

        return JsonResponse({'recipe': recipes_result}, status=200)