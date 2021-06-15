import json
import bcrypt

from django.views     import View
from django.http      import JsonResponse

from .models   import Cart
from .models   import Ingredient
from .models   import User 
from user      import login_decorator

class CartListView(View):
    @login_decorator
    def post(self,request):
        try:
            data = json.loads(request.body)

            if data['count'] <= 0:
                return JsonResponse({"message": "LESS_THAN_MINIMUM_QUANTITY"}, status=400)

            Cart.objects.create(
                count        =data['count'],
                ingredient_id=data['ingredient_id'],
                user_id      =data['user_id']
                )
            return JsonResponse({'message':'SUCCESS'}, status=201)
   
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)


    @login_decorator
    def get(self,request):
        try:
            users = login_decorator.user
            
            user_id_to_ingeridient = Cart.objects.filter(user_id=users) 
            #데코레이터로 확인한 유저의 장바구니 품목 조회 (Cart queryset)
            

            #for ingredients in carts :



        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

    
    # def delete(self,request):
    #      try:
    #          data = json.loads(request.body)



    #      except KeyError:
    #          return JsonResponse({"message": "KEY_ERROR"}, status=400)
