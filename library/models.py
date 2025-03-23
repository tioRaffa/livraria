from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    type_category = models.CharField(("Tipo Categoria"), max_length=50)
    
    def __str__(self):
        return self.type_category

    def get_absolute_url(self):
        return reverse("_category", kwargs={"pk": self.pk})



class BookModel(models.Model):
    title = models.CharField(("Titulo"), max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.CharField(("Autor"), max_length=150)
    release_date = models.DateField(("Data de Lançamento"), null=True, blank=True)
    description = models.TextField(("Descrição"))
    pages = models.IntegerField(("Paginas"))
    image = models.ImageField(("Imagem"), upload_to='library/books/%y/%m/%d',)
    is_published = models.BooleanField(("Publicado"), default=False)
    bestseller = models.BooleanField(("BestSeller"), null=True, default=False)
    purchase_link = models.URLField(("Link de Compra"), max_length=200, null=True)
    
    def __str__(self):
        return self.title