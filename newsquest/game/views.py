from django.shortcuts import render
from django.http import HttpResponse as hr

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Create your views here.
def world(request):
    return render(request, 'world.html')

def highscores(request):
    # select 10 highest scores and send them with their username to the template
    queries = CustomUser.objects.all().order_by('-points').values('name', 'points')[:10]
    context = {
        "users": list(queries)
    }
    return render(request, 'highscores.html', context=context)

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'