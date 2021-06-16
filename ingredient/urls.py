from django.urls import path
from django.views.generic.base import View

from .views import IngredientsView

urlpatterns = [
    path('', IngredientsView.as_view()),
    path('/ingredient',IngredientsView.as_view()),
]