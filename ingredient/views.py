from django.http       import JsonResponse
from django.views      import View
from recipe.models     import Recipe
from ingredient.models import Ingredient


class ShowIngredientInfo(View):
    def get (self,request): 
        try:
            request_id  = request.GET.get('id',None)
            ingredient  = Ingredient.objects.get(id = request_id) 
            recipe_info = Recipe.objects.filter(ingredientrecipe__ingredient = request_id) 
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
        except Exception as e:
            print(e)
            return JsonResponse({"message":"INVALID"})
        
class ShowRecipeInfo(View):
    def get (self,request): 
        try:
            request_id      = request.GET.get('id',None)
            recipe          = Recipe.objects.get(id = request_id) 
            ingredient_info = Ingredient.objects.filter(ingredientrecipe__recipe = request_id) 
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
        except Exception as e:
            print(e)
            return JsonResponse({"message":"INVALID"})