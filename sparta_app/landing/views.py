from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, RedirectView
from django.urls import reverse_lazy
from .forms import RegisterUserForm, UserAuthenticationForm
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalLoginView

class IndexView(TemplateView):
    template_name = "landing/home_page.html"
    

class RegisterView(BSModalCreateView):
    form_class = RegisterUserForm
    template_name = "landing/signup.html"
    success_message = 'Sign up succeeded. Now Click "Take Exam" to Login.'
    success_url = reverse_lazy("index")

class UserLoginView(BSModalLoginView):
    authentication_form = UserAuthenticationForm
    template_name = 'landing/login.html'
    success_message = 'You were successfully logged in.'
    extra_context = dict(success_url=reverse_lazy('quiz_index'))

    

class LogoutView(RedirectView):
    url = reverse_lazy('index')
    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)