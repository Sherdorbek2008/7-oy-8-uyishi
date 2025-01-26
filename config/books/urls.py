from django.urls import path
from .views import Index, Detail, Book_By_Ganer, Book_Add, Book_Update, Book_Delete

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('detail/<int:book_id>/', Detail.as_view(), name='book_detail'),
    path('genre/<int:genre_id>/', Book_By_Ganer.as_view(), name='books_by_genre'),
    path('book/add/', Book_Add.as_view(), name='add_book'),
    path('book/<int:book_id>/update/', Book_Update.as_view(), name='update_book'),
    path('book/<int:book_id>/delete/', Book_Delete.as_view(), name='delete_book'),
]
