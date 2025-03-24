from django.views.generic import ListView
from .models import BookModel, Category


class HomeView(ListView):
    model = BookModel
    queryset = BookModel.objects.filter(is_published=True).order_by('?')
    template_name = 'pages/home.html'
    context_object_name = 'books'
    
    paginate_by = 4
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category = Category.objects.all()
        best = BookModel.objects.filter(bestseller=True, is_published=True)
        
        context.update({
            'categories': category,
            'bestsellers': best
        })
        
        return context