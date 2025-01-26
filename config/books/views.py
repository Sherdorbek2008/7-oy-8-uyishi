from django.contrib import messages
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Ganer, Book
from .forms import BookForm


class Index(ListView):
    model = Book
    template_name = 'index.html'
    context_object_name = 'books'
    extra_context = {
        'title': "Asosiy Sahifa"
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['genres'] = Ganer.objects.all()
        return context


class Detail(DetailView):
    model = Book
    pk_url_kwarg = 'book_id'
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['book'] = get_object_or_404(Book, pk=self.kwargs.get('book_id'))
        return context


class Book_By_Ganer(ListView):
    model = Book
    template_name = 'index.html'
    context_object_name = 'books'
    paginate_by = 3

    def get_queryset(self):
        genre_id = self.kwargs.get('genre_id')
        if genre_id:
            return Book.objects.filter(genre_id=genre_id)
        return Book.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        genre_id = self.kwargs.get('genre_id')
        if genre_id:
            genre = get_object_or_404(Ganer, pk=genre_id)
            context['selected_genre'] = genre
        else:
            context['selected_genre'] = None
        context['genres'] = Ganer.objects.all()
        return context


class Book_Add(CreateView):
    model = Book
    template_name = 'add_book.html'
    form_class = BookForm
    extra_context = {'title': "Kitob qo'shish"}

    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'book_id': self.object.id})

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Kitob muvaffaqiyatli tarzda qo'shildi!")
        return response


class Book_Update(UpdateView):
    model = Book
    template_name = 'add_book.html'
    form_class = BookForm
    pk_url_kwarg = 'book_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"{self.object.title}: tahrirlash!"
        return context

    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'book_id': self.object.id})

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Kitob muvaffaqiyatli tarzda tahrirlandi!")
        return response


class Book_Delete(DeleteView):
    model = Book
    pk_url_kwarg = 'book_id'
    success_url = reverse_lazy('home')
    template_name = 'confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['book'] = get_object_or_404(Book, pk=self.kwargs.get('book_id'))
        context['title'] = f"{self.object.title}: o'chirish!"
        return context

    def get(self, request, *args, **kwargs):
        messages.warning(request, "Ushbu kitobni o'chirishni xohlaysizmi?")
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Kitob muvaffaqiyatli tarzda o'chirildi!")
        return response