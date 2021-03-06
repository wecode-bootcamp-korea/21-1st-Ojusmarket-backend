import json

from django.views import View
from django.http import JsonResponse
from django.db import transaction

from cart.models import Cart
from .models import Order, OrderItem, OrderStatus

from user.utils import login_decorator

class PaymentView(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            with transaction.atomic():
                cart_ingredient = [cart["id"] for cart in data["cart"]]
                carts = Cart.objects.filter(user_id = request.user.id, ingredient_id__in = cart_ingredient)

                Order.objects.create(
                    address   = data["address"],
                    status_id = OrderStatus.objects.get(id=1).id
                )

                new_order = Order.objects.last()
                for cart in carts:
                    OrderItem.objects.create(
                        order_id = new_order.id,
                        cart_id  = cart.id
                    )

                return JsonResponse({"message": "CREATED"}, status = 201)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status = 400)