from django.urls import path

from .views import CartListView

urlpatterns = [
    path('/cart_list', CartListView.as_view())
]