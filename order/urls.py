from django.urls import path

from .views import OrderpageView, PaymentView

urlpatterns = [
    path('/order', OrderpageView.as_view()),
    path('/payment', PaymentView.as_view())
]