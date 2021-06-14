from django.core.exceptions import ObjectDoesNotExist
from django.http            import JsonResponse
from django.views           import View
from recipe.models          import Recipe
from ingredient.models      import Ingredient


class IngredientInfo(View):
    def get (self,request,ingredient_id): 
        try:
            ingredient  = Ingredient.objects.get(id = ingredient_id) 
            recipe_info = Recipe.objects.filter(ingredientrecipe__ingredient = ingredient_id) 
            recipe_list = [{
                "id"        : recipe.id,
                "name"      : recipe.name,
                "image_url" : recipe.image_url} for recipe in recipe_info] 
            info_dict ={
                "id"        : ingredient.id,
                "name"      : ingredient.name,
                "price"     : ingredient.price,
                "storage"   : ingredient.storage,
                "image_url" : ingredient.image_url,
                "related"   : recipe_list
            }
            return JsonResponse({"ingredients":info_dict})
        except ObjectDoesNotExist:
            return JsonResponse({"message":"Object does not exist"})