from django import forms
from .models import Ganer, Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'slug', 'description', 'price', 'image', 'ganer']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': "Kitob nomini kiriting",
                'class': 'form-control'
            }),

            'slug': forms.Textarea(attrs={
                'rows': "slug ni kiriting",
                'class': 'form-control'
            }),

            'description': forms.TextInput(attrs={
                'placeholder': "Kitob haqida malumot kiriting",
                'class': 'form-control'
            }),

            'price': forms.NumberInput(attrs={
                'placeholder': "Kitob narxini kiriting",
                'class': 'form-control'
            }),

            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),

            'ganer': forms.Select()
        }
