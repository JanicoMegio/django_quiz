from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import RegisterUserForm


class IndexView(TemplateView):
    template_name = "landing/home_page.html"
    

class RegisterView(CreateView):
    form_class = RegisterUserForm
    template_name = "landing/home_page.html"
    success_url = reverse_lazy("quiz_index")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

