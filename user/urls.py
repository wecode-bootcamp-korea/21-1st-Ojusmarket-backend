from django.urls import path
from .views import UserIdentityCheck
from .views import UserSignUp , SigninView
urlpatterns = [
    path('/idCheck', UserIdentityCheck.as_view()),
    path('/signUp', UserSignUp.as_view())
    path('/signin', SigninView.as_view())
     ]
