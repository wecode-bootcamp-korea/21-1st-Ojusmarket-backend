from django.urls import path
from ingredient.views import ShowIngredientInfo, ShowRecipeInfo

urlpatterns = [
    path('/detail',ShowRecipeInfo.as_view()),
    path('/detail',ShowIngredientInfo.as_view()),
]
