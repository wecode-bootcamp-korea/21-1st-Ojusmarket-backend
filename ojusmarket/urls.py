from django.urls import path, include

urlpatterns = [
    path('user', include('user.urls')),
    path('ingredients', include('ingredient.urls')),
    path('recipes', include('recipe.urls')),
]