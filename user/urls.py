from django.urls import path

from .views import UserIdentityCheck
from .views import UserSignUp, SigninView, UserView
urlpatterns = [
    path('/id-check', UserIdentityCheck.as_view()),
    path('/sign-up', UserSignUp.as_view()),
    path('/sign-in', SigninView.as_view()),
    path('', UserView.as_view())
]