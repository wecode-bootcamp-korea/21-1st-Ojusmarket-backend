from django.http      import JsonResponse
from django.views     import View
from recipe.models    import Recipe
from django.db.models import Q
from recipe.models    import Recipe  


class RecipesView(View):
    def get(self, request):
        category_id = request.GET.get('category_id', None)

        q = Q()
        if category_id:

            q &= Q(category_id=category_id)

        recipes = Recipe.objects.filter(q)
        
        results = []

        for recipe in recipes:
            results.append({
                'id'          : recipe.id,
                'name'        : recipe.name,
                'image_url'   : recipe.image_url,
                'category_id' : recipe.category_id
            })

        return JsonResponse({'recipes': results}, status=200)   

class RecipeView(View):
    def get (self, request, recipe_id): 
        try:
            recipe = Recipe.objects.get(id=recipe_id)
            result = {
                "id"                  : recipe.id,
                "name"                : recipe.name,
                "image_url"           : recipe.image_url, 
                "related_ingredients" : [{
                    "id"        : ingredient.id,
                    "name"      : ingredient.name,
                    "image_url" : ingredient.image_url,
                    "price"     : ingredient.price
                    } for ingredient in recipe.ingredient_set.all()]
            }
            return JsonResponse({"recipe":result})
        except Recipe.DoesNotExist:
            return JsonResponse({"message":"Object does not exist"})         
        
