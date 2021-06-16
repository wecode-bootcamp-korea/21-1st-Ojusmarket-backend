from django.http            import JsonResponse
from django.views           import View
from ingredient.models      import Ingredient
from django.db.models       import Q


class IngredientsView(View):
    def get(self, request):
        category_id = request.GET.get('category_id', None)
        
        q = Q()
        
        if category_id:
            q &= Q(category_id=category_id)

        ingredients = Ingredient.objects.filter(q)

        result = []

        for ingredient in ingredients:
            result.append({
                'id'          : ingredient.id,
                'name'        : ingredient.name,
                'price'       : ingredient.price,
                'storage'     : ingredient.storage,
                'category_id' : ingredient.category.main_category_id,
                'image_url'   : ingredient.image_url
            })

        return JsonResponse({'ingredients' : result}, status=200)
        
class IngredientView(View):
    def get (self, request, ingredient_id): 
        try: 
            ingredient  = Ingredient.objects.get(id=ingredient_id)
            recipe_all  = ingredient.recipe.all()
            result = {
                "id"               : ingredient.id,
                "name"             : ingredient.name,
                "price"            : ingredient.price,
                "info"             : ingredient.info,
                "storage"          : ingredient.storage,
                "image_url"        : ingredient.image_url,
                "related_recipes"   : [{
                                        "id"        : recipe.id,
                                        "name"      : recipe.name,
                                        "image_url" : recipe.image_url} for recipe in recipe_all]
            }
            return JsonResponse({"ingredient":result})
        except Ingredient.DoesNotExist:
            return JsonResponse({"message":"Object does not exist"})