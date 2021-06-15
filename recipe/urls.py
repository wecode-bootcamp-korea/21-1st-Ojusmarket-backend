from django.urls import path
from django.views.generic.base import View
from .views import RecipesView

urlpatterns = [
    path('',RecipesView.as_view()),
    path('/recipe',RecipesView.as_view())
]
