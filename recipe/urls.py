from django.urls import path
from .views      import RecipesView, RecipeView

urlpatterns = [
    path('', RecipesView.as_view()),
    path('/recipe', RecipesView.as_view()),
    path('/<int:recipe_id>', RecipeView.as_view()),
]
