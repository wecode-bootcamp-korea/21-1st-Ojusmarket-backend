from django.urls import path
from django.views.generic.base import View
from .views import MaincategoryView

urlpatterns = [
    path('/main',MaincategoryView.as_view()),
]
