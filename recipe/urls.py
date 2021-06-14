from django.urls import path
from django.views.generic.base import View
from .views import RecipesView,RecipecategoriesView

urlpatterns = [
    path('',RecipesView.as_view()),
    path('/recipe',RecipecategoriesView.as_view())
]
