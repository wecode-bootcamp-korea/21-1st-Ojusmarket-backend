from django.core.exceptions import ObjectDoesNotExist
from django.http            import JsonResponse
from django.views           import View
from recipe.models          import Recipe
from ingredient.models      import Ingredient


class RecipeInfo(View):
    def get (self,request,recipe_id): 
        try:
            recipe          = Recipe.objects.get(id = recipe_id) 
            ingredient_info = Ingredient.objects.filter(ingredientrecipe__recipe = recipe_id) 
            ingredient_list = [{
                "id"        : ingredient.id,
                "name"      : ingredient.name,
                "image_url" : ingredient.image_url} for ingredient in ingredient_info]
            info_dict = {
                "id"        : recipe.id,
                "name"      : recipe.name,
                "image_url" : recipe.image_url, 
                "related"   : ingredient_list
            }
            return JsonResponse({"recipe":info_dict})
        except ObjectDoesNotExist:
            return JsonResponse({"message":"Object does not exist"})         