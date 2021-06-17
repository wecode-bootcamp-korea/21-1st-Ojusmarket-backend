from django.urls import path

from .views import OrderpageView, PaymentView

urlpatterns = [
    path('', OrderpageView.as_view()),
    path('/payment', PaymentView.as_view())
]