import json, bcrypt

from django.views     import View
from django.http      import JsonResponse

from .models   import Cart

from utils import login_decorator

class CartListView(View):
    @login_decorator
    def post(self,request):
        try:
            data = json.loads(request.body)
            user = request.user

            if data['count'] <= 0:
                return JsonResponse({"message": "LESS_THAN_MINIMUM_QUANTITY"}, status=400) 

            if Cart.objects.filter(user=user, ingredient_id=data['ingredient_id']).exists() :#queryset
                cart = Cart.objects.get(user=user, ingredient_id=data['ingredient_id'])
                cart.count += data['count']
                cart.save()
                return JsonResponse({'message':'ADDITIONAL_SUCCESS'}, status=200) 
                    
            Cart.objects.create(
                    count         = data['count'],
                    ingredient_id = data['ingredient_id'],
                    user          = user
                    )
            return JsonResponse({'message':'SUCCESS'}, status=201)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        
        except Cart.DoesNotExist:
          return JsonResponse({'message': 'THIS_ACCOUNT_DOES_NOT_EXIST'}, status=400)
    
    @login_decorator
    def get(self,request):
        try:
            users_ingredient_list = Cart.objects.filter(user=request.user)
            cart_list = []

            for cart in users_ingredient_list :
                cart_info = {
                    'id'       : cart.ingredient.id,
                    'name'     : cart.ingredient.name,
                    'price'    : cart.ingredient.price,
                    'image_url': cart.ingredient.image_url,
                    'count'    : cart.count
                }
                cart_list.append(cart_info)

            return JsonResponse({'cart_list':cart_list}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except Cart.DoesNotExist:
          return JsonResponse({'message': 'THIS_ACCOUNT_DOES_NOT_EXIST'}, status=400)

    # def delete(self,request):
    #      try:
    #         data = json.loads(request.body)
    #         user = request.user

    #         ingredient_info    = Cart.objects.filter(user_id=user)
    #         ingredient_id_list = [] 
            
    #         for ingredient_id in ingredient_info :
    #             ingredient_id_list.append(ingredient_id['ingredient_id'])

    #         for id_delete in ingredient_id_list:
    #             Cart.objects.filter(ingredient_id=id_delete).delete()
    #         return JsonResponse({'message': 'SUCCESSFUL_DELETION'}, status=200)
    #         #필터 쿼리셋 자체를 삭제함으로 한번에 모아진 쿼리셋을 삭제할 수 있는 방법 찾기    

    #      except KeyError:
    #          return JsonResponse({"message": "KEY_ERROR"}, status=400)