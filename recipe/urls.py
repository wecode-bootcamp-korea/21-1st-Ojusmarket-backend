from django.urls  import path
from recipe.views import RecipeView

urlpatterns = [
    path('/<int:recipe_id>', RecipeView.as_view()),
]
