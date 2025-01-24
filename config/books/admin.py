from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# Register your models here.




@admin.register(Ganer)
class DepartamentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_display_links = ('name',)






@admin.register(Book)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'name', 'slug', 'description', 'price','ganer','image')
    def get_image(self, Book):
        images = Book.image_set.all()
        if images:
            return mark_safe(f'<img src="{images[0], images.url}" width="100"')
        return ''
