from django.views import View
from django.http import JsonResponse
from django.db.models  import Q

from recipe.models import Recipe  

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
        