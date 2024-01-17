from django.urls import path, include
from .views import RegisterView, IndexView, UserLoginView, LogoutView



urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('Signup', RegisterView.as_view(), name="signup"),
    path('Login', UserLoginView.as_view(), name="login"),
    path('logout',LogoutView.as_view(), name='logout'),
    path('Quiz', include('quiz.urls')),
]



