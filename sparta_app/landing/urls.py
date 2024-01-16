from django.urls import path, include
from .views import RegisterView, IndexView, UserLoginView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('Register', RegisterView.as_view(), name="register"),
    path('Login', UserLoginView.as_view(), name="login"),
    path('TakeExam', include('quiz.urls')),
]



