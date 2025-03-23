from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('detail/<int:id>', views.DetailBook.as_view(), name='detail_book')
]
