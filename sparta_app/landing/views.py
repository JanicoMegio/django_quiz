from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import RegisterUserForm, UserAuthenticationForm
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalLoginView

class IndexView(TemplateView):
    template_name = "landing/home_page.html"
    

class RegisterView(BSModalCreateView):
    form_class = RegisterUserForm
    template_name = "landing/register.html"
    success_message = 'Success: Sign up succeeded. WELCOME!'
    success_url = reverse_lazy("quiz_index")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class UserLoginView(BSModalLoginView):
    authentication_form = UserAuthenticationForm
    template_name = 'landing/login.html'
    success_message = 'Success: You were successfully logged in.'
    extra_context = dict(success_url=reverse_lazy('quiz_index'))