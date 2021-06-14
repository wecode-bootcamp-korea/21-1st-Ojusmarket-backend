from django.urls import path
from django.views.generic.base import View

from .views import IngredientsView, IngredientcategoriesView

urlpatterns = [
    path('', IngredientsView.as_view()),
    path('/ingredient',IngredientcategoriesView.as_view()),
]


"http://:8000/ingredients"
"http://:8000/ingredients?category_id=1"
"http://:8000/ingredients/<ingredient_id>"
"http://:8000/ingredients/1"
