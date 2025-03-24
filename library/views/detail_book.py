from django.views.generic import DetailView
from .models import BookModel, Category
from django.shortcuts import get_object_or_404


class DetailBook(DetailView):
    model = BookModel
    template_name = 'pages/detail_page.html'
    context_object_name = 'book'
    
    def get_object(self, queryset=None):
        return get_object_or_404(BookModel, id=self.kwargs['id'], is_published=True)
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        best = BookModel.objects.filter(bestseller=True, is_published=True)
        
        context.update({
            'categories': Category.objects.all(),
            'bestsellers': best
        })
        return context