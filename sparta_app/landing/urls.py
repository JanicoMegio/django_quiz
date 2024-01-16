from django.urls import path, include
from .views import RegisterView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('Register', RegisterView.as_view(), name="register"),
    path('TakeExam', include('quiz.urls')),
]



