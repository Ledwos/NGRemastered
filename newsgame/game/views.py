from django.shortcuts import render
from django.http import HttpResponse as hr

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.

def index(request):
    return hr('me llamo index')

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'