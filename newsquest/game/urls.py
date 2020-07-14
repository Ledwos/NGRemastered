from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

#app_name = 'game'
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

