from django.views import View
from django.http import JsonResponse
from django.db.models  import Q

from ingredient.models import Ingredient

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