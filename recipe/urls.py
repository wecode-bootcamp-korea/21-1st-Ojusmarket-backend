from django.urls import path
from recipe.views import RecipeInfo

urlpatterns = [
    path('/<int:recipe_id>',RecipeInfo.as_view()),
]
