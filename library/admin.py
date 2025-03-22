from django.contrib import admin
from .models import BookModel, Category
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'type_category'
    ]
    ordering = ['-id']



@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'author',
        'release_date',
        'category',
        'is_published'
    ]
    ordering = ['-id']
    list_display_links = [
        'id',
        'title',
        'author'
    ]