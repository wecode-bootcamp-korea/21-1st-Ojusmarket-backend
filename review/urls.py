from django.urls import path

from .views import ReviewView

urlpatterns = [
    path('/<int:ingredient_id>', ReviewView.as_view())
]