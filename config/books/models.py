from django.db import models


# Create your models here.

class Ganer(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='nomi')
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name




class Book(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='nomi')
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(null=True, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='books/images/')
    ganer = models.ForeignKey(Ganer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

