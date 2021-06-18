import json

from django.views     import View
from django.http      import JsonResponse

from .models import Cart
from utils   import login_decorator

class CartListView(View):

    @login_decorator
    def post(self,request):
        try:
            data = json.loads(request.body)
            user = request.user

            if data['count'] <= 0:
                return JsonResponse({"message": "LESS_THAN_MINIMUM_QUANTITY"}, status=400) 

            if Cart.objects.filter(user=user, ingredient_id=data['id'],soft_delete=False).exists():
                cart = Cart.objects.get(user=user, ingredient_id=data['id'])
                cart.count += data['count']
                cart.save()
                return JsonResponse({'message':'ADDITIONAL_SUCCESS'}, status=200) 
                    
            Cart.objects.create(
                count         = data['count'],
                ingredient_id = data['id'],
                user          = user
                )
            return JsonResponse({'message':'SUCCESS'}, status=200)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
    
    @login_decorator
    def get(self,request):
        try:
            carts = Cart.objects.filter(user=request.user,soft_delete=False)
            cart_list = []

            for cart in carts:
                cart_list.append({
                    'id'       : cart.ingredient.id,
                    'name'     : cart.ingredient.name,
                    'price'    : cart.ingredient.price,
                    'image_url': cart.ingredient.image_url,
                    'count'    : cart.count
                    })    
            return JsonResponse({'cart_list':cart_list}, status=200)

        except Cart.DoesNotExist:
            return JsonResponse({"message": "DOSE_NOT_EXIST"}, status=400)

    @login_decorator
    def delete(self,request):
        try:
            data = json.loads(request.body)
            user = request.user
            
            Cart.objects.filter(user_id=user.id, ingredient_id__in=data).delete()
            return JsonResponse({"message": "SUCCESSFUL_DELETION"}, status=204)

        except Cart.DoesNotExist:
            return JsonResponse({"message": "DOSE_NOT_EXIST"}, status=400)

    @login_decorator
    def patch(self,request):
        try:
            data = json.loads(request.body)
            
            for data_i in data:
                cart = Cart.objects.get(user=request.user, ingredient_id=data_i['id'])
                Cart.objects.filter(user=request.user, ingredient_id=data_i['id'], count=cart.count).update(count=data_i['count'])
            return JsonResponse({"message": "SUCCESSFUL_UPDATE"}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
