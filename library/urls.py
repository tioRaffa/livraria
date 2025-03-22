from django.urls import path
from . import views

APP_NAME = 'library'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
]
