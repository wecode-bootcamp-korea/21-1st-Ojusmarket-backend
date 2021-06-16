from django.urls import path

from .views import CartListView

urlpatterns = [
    path('/list', CartListView.as_view())
]