import json

from django.views import View
from django.http import JsonResponse

from recipe.models import Recipe

class RecipecategoriesView(View):
    def get(self, request, category_id):

        category_id = request.GET['recipe_cateogry']

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

class RecipesView(View):
    def get(self, request):

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