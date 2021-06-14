from django.urls import path
from ingredient.views import IngredientInfo

urlpatterns = [
    path('/<int:ingredient_id>',IngredientInfo.as_view()),
]
