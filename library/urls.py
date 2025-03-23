from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('detail/<int:id>', views.DetailBook.as_view(), name='detail_book'),
    path('bestsellar/<int:id>', views.DetailBook.as_view(), name='bestseller_book'),
    path('category/<int:id>', views.CategoryBook.as_view(), name='category_book'),
]
