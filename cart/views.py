import json, bcrypt

from django.views     import View
from django.http      import JsonResponse

from .models   import Cart, Ingredient, User

from utils import login_decorator

class CartListView(View):
    @login_decorator
    def post(self,request):
        try:
            data = json.loads(request.body)
            user = request.user

            if data['count'] <= 0:
                return JsonResponse({"message": "LESS_THAN_MINIMUM_QUANTITY"}, status=400)

            duplicate_user = Cart.objects.filter(user_id=user.id)

            for cart in duplicate_user :
                if cart.ingredient_id == data['ingredient_id'] :
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
          return JsonResponse({'message': 'THIS ACCOUNT DOES NOT EXIST'}, status=400)
    
    @login_decorator
    def get(self,request):
        try:
            user = request.user
            
            users_ingredient_list = Cart.objects.filter(user_id=user)
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
          return JsonResponse({'message': 'THIS ACCOUNT DOES NOT EXIST'}, status=400)

    # def delete(self,request):
    #      try:
    #          data = json.loads(request.body)
    #      except KeyError:
    #          return JsonResponse({"message": "KEY_ERROR"}, status=400)