import json, ingredient

from django.views import View
from django.http import JsonResponse

from .models import Order, OrderStatus
from user.models import User
from cart.models import Cart

from utils import login_decorator

class OrderpageView(View):
    @login_decorator
    def post(self, request, ingredient_id):
        try:
            data   = json.loads(request.body)
            user   = request.user
            cart   = Cart.objects.filter(user=user)
            
            if not cart.exists():
                return JsonResponse({'message' : 'CART_DOES_NOT_EXIST'}, status=400)
            
            order_info  = Order.objects.create(
                cart    = Cart.objects.filter(user=user),
                status  = OrderStatus.objects.get(id=1),
                address = data.get('address', cart.user.address)
            )

            return JsonResponse({"message" : "SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({'message' : 'KEYERROR'}, status= 400)

    @login_decorator
    def get(self, request):
        try:
            user = request.user
            cart = Cart.objects.filter(user=user)
            order = Order.objects.get(user=user)
        
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
            order = Order.objects.get(user=user)
            cart = Cart.objects.filter(user=user)

            payment_list = [{
                'name' : order.cart.user.name,
                'address' : order.cart.user.address,
                'price' : order.cart.ingredient.price * 
            }]


        except KeyError:
            JsonResponse({'message' : 'KEYERROR'}, status=400)
