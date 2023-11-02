from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.showing_list_of_books, name="showing_list_of_books"),
    path('authors/', views.all_authors_list, name="all_authors_list"),
    path('<int:book_id>/', views.book_detail, name="book_detail"),
    path('books/author/<int:author_id>/', views.author_detail, name="author_detail"),
    path('book/authos/booksofauthor/<int:author_id>', views.get_all_books_of_author, name="author_books")
]
