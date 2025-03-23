from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from .models import BookModel, Category
from django.shortcuts import get_object_or_404

# Create your views here.
class HomeView(ListView):
    model = BookModel
    queryset = BookModel.objects.filter(is_published=True).order_by('-id')
    template_name = 'pages/home.html'
    context_object_name = 'books'
    
    paginate_by = 4
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        books = BookModel.objects.filter(is_published=True).order_by('-id')
        category = Category.objects.all()
        
        context.update({
            'categories': category
        })
        
        return context
    
    
    
class DetailBook(DetailView):
    model = BookModel
    template_name = 'pages/detail_page.html'
    context_object_name = 'book'
    
    def get_object(self, queryset=None):
        return get_object_or_404(BookModel, id=self.kwargs['id'], is_published=True)
    

class CategoryBook(ListView):
    model = BookModel
    template_name = 'pages/category_page.html'
    paginate_by = 4
    
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        
        queryset = queryset.filter(
            category__id=self.kwargs.get('id'),
            is_published=True
        ).order_by('-id')
        
        return queryset
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        books = BookModel.objects.filter(is_published=True).order_by('-id')
        category = Category.objects.all()
        
        context.update({
            'books': books,
            'categories': category
        })
        
        return context
    