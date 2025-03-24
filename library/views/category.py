from .home import HomeView
from .models import BookModel, Category


class CategoryBook(HomeView):
    model = BookModel
    template_name = 'pages/category_page.html'
    paginate_by = 4
    context_object_name = 'books'
    
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        
        queryset = queryset.filter(
            category__id=self.kwargs.get('id'),
            is_published=True
        ).order_by('?')
        
        return queryset
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        best = BookModel.objects.filter(bestseller=True, is_published=True)
        
        
        context.update({
            'categories': Category.objects.all(),
            'bestsellers': best
        })
        return context