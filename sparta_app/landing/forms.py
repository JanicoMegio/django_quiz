from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class RegisterUserForm(PopRequestMixin, CreateUpdateAjaxMixin, UserCreationForm):

    first_name = forms.CharField(max_length=30, help_text="Enter your First Name")
    last_name = forms.CharField(max_length=30, help_text="Enter your Last Name")
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1']
        

class UserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']