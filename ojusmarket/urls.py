from django.urls import path, include

urlpatterns = [
    path('user', include('user.urls')),
    path('ingredient',include('ingredient.urls')),
    path('recipe',include('ingredient.urls')),
]