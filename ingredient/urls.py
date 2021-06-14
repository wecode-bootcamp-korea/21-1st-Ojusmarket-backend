from django.urls import path
from ingredient.views import IngredientView

urlpatterns = [
    path('/<int:ingredient_id>',IngredientView.as_view()),
]
