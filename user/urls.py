from django.urls import path
from .views      import SignupView, SigninView

urlpatterns = [
    path('/signup', SignupView.as_view()),
    path('/sigin', SigninView.as_view())
]

