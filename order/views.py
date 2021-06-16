import json

from django.views import View
from django.http import JsonResponse

from user.models import User
from cart.models import Cart

from user.utils import login_decorator

class OrderpageView(View):
    @login_decorator
    def get(self, request):
        try:
            user = request.user
            cart= Cart.objects.filter(user=user)

            user_list = [{
                'name'    : user.name,
                'phone'   : user.phone,
                'address' : user.address
            }]

            return JsonResponse({'user' : user_list}, status=200)

        except KeyError:
            JsonResponse({'message' : 'KEYERROR'}, status=400)

class PaymentView(View):
    @login_decorator
    def get(self, request):
        try:
            user = request.user
            
            total = 0

            for a in user.cart_set.all():

                total += a.ingredient.price * a.count

            payment_list = [{
                'name'    : user.name,
                'address' : user.address,
                'price'   : total
            }]

            Cart.objects.filter(user=user).delete()

            return JsonResponse({'payment' : payment_list}, status=200)

        except KeyError:
            JsonResponse({'message' : 'KEYERROR'}, status=400)