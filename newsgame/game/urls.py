from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from . import views

#app_name = 'game'
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('user/', include('django.contrib.auth.urls')),
    #path('<int:question_id>/', views.detail, name='detail'),
]

