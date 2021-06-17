from django.urls      import path
from ingredient.views import IngredientsView,IngredientView

urlpatterns = [
    path('', IngredientsView.as_view()),
    path('/ingredient',IngredientsView.as_view()),
    path('/<int:ingredient_id>', IngredientView.as_view()),
]

