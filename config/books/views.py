from django.views.generic import ListView
from .models import Book, Ganer

class booksListView(ListView):
    model = Book
    context_object_name = "books"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context["department"] = Ganer.objects.all()
        return context


