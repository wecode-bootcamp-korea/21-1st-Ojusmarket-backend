from django.core.exceptions import ObjectDoesNotExist
from django.http            import JsonResponse
from django.views           import View
from ingredient.models      import Ingredient


class IngredientView(View):
    def get (self, request, ingredient_id): 
        try: 
            ingredient  = Ingredient.objects.get(id=ingredient_id)
            recipe_all  = ingredient.recipe.all()
            recipe_list = [{
                "id"        : recipe.id,
                "name"      : recipe.name,
                "image_url" : recipe.image_url} for recipe in recipe_all]
            result = {
                "id"               : ingredient.id,
                "name"             : ingredient.name,
                "price"            : ingredient.price,
                "info"             : ingredient.info,
                "storage"          : ingredient.storage,
                "image_url"        : ingredient.image_url,
                "related_recipe"   : recipe_list
            }
            return JsonResponse({"ingredient":result})
        except ObjectDoesNotExist:
            return JsonResponse({"message":"Object does not exist"})