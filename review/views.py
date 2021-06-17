import json

from django.views import View
from django.http  import JsonResponse

from .models           import Review
from user.models       import User
from ingredient.models import Ingredient
from user.utils        import login_decorator

#리뷰 생성 
class ReviewView(View):
    @login_decorator
    def post(self, request, ingredient_id): 
        try:
            data = json.loads(request.body)
            
            if not Ingredient.objects.filter(id = ingredient_id).exists():
                return JsonResponse({'message': 'INVALID_INGREDIENT'}, status=400) 

            Review.objects.create(
            text       = data['text'],
            user       = request.user,
            ingredient_id = ingredient_id
            )
        
            return JsonResponse({'message': 'CREATED'}, status=201) 

        except KeyError:
            return JsonResponse({'message': 'INVALID_KEY_ERROR'}, status=400)