from django.shortcuts import render
from django.views.generic import View, ListView
from .models import BookModel
# Create your views here.
class HomeView(ListView):
    model = BookModel
    queryset = BookModel.objects.filter(is_published=True).order_by('-id')
    template_name = 'pages/home.html'
    context_object_name = 'books'
    
    paginate_by = 5