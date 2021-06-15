from django.core.exceptions import ObjectDoesNotExist
from django.http            import JsonResponse
from django.views           import View
from recipe.models          import Recipe



class RecipeView(View):
    def get (self, request, recipe_id): 
        try:
            recipe          = Recipe.objects.get(id=recipe_id) 
            ingredient_all = recipe.ingredient_set.all()
            ingredient_list = [{
                "id"        : ingredient.id,
                "name"      : ingredient.name,
                "image_url" : ingredient.image_url,
                "price"     : ingredient.price} for ingredient in ingredient_all]
            result = {
                "id"                 : recipe.id,
                "name"               : recipe.name,
                "image_url"          : recipe.image_url, 
                "related_ingredient" : ingredient_list
            }
            return JsonResponse({"recipe":result})
        except ObjectDoesNotExist:
            return JsonResponse({"message":"Object does not exist"})         