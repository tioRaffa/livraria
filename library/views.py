from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from .models import BookModel
from django.shortcuts import get_object_or_404

# Create your views here.
class HomeView(ListView):
    model = BookModel
    queryset = BookModel.objects.filter(is_published=True).order_by('-id')
    template_name = 'pages/home.html'
    context_object_name = 'books'
    
    paginate_by = 4
    
    
class DetailBook(DetailView):
    model = BookModel
    template_name = 'pages/detail_page.html'
    context_object_name = 'book'
    
    def get_object(self, queryset=None):
        return get_object_or_404(BookModel, id=self.kwargs['id'], is_published=True)