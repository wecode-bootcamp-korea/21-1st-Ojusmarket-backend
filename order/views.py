import json, ingredient

from django.views import View
from django.http import JsonResponse

from .models import Order, OrderStatus
from user.models import User
from cart.models import Cart

from user.utils import login_decorator

class OrderpageView(View):
    @login_decorator
    def post(self, request):
        try:
            data   = json.loads(request.body)
            user   = request.user
            cart  = Cart.objects.filter(user=user)
            status = OrderStatus.objects.get(id=1)
            
            if not Order.objects.filter(address = data['address']).exists:
            
                return JsonResponse({'message' : 'ADDRESS_DOSE_NOT_EXIST'}, status=400)
            
            order_info  = Order.objects.create(
                cart    = cart[0],
                status  = status,
                address = data['address']
            )
    
            return JsonResponse({"message" : "SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({'message' : 'KEYERROR'}, status= 400)

    @login_decorator
    def get(self, request):
        try:
            user = request.user
            cart = Cart.objects.get(user=user)
        
            user_list = [{
                'name'    : cart.user.name,
                'phone'   : cart.user.phone,
                'address' : cart.user.address
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
            cart = Cart.objects.get(user=user)

            payment_list = [{
                'name' : order.cart.user_id.name,
                'address' : order.cart.user_id.address,
                'price' : order.cart.ingredient.price * cart.count
            }]

            return JsonResponse({'payment' : payment_list}, status=200)

        except KeyError:
            JsonResponse({'message' : 'KEYERROR'}, status=400)

