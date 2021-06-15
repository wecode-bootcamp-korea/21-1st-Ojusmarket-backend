from django.views import View
from django.http import JsonResponse
from django.db.models  import Q

from recipe.models import Recipe  

class RecipesView(View):
    
    def get(self, request):
        category_id = request.GET.get('category_id', None)

        # CASE 1
        q = Q()
        if category_id:
            q &= Q(category_id=category_id)
        recipes = Recipe.objects.filter(q)


        # CASE 2
        # recipes = Recipe.objects.all()

        # if category_id:
        #     recipes = recipes.filter(category_id=category_id)

        results = []

        for recipe in recipes:
            results.append({
                'id'          : recipe.id,
                'name'        : recipe.name,
                'image_url'   : recipe.image_url,
                'category_id' : recipe.category_id
            })

        return JsonResponse({'recipes': results}, status=200)   
        