from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader

from .models import Author, Book


def index(request):
    return HttpResponse('You are at book route 😀')


# Create your views here.

def get_all_authors():
    authors = Author.objects.all()
    return authors


def get_all_books_of_author(request, author_id=1):
    books = Book.objects.filter(author__id=author_id)
    template_response = loader.get_template('authors/books_of_author.html')
    return HttpResponse(template_response.render({'books': books}, request))


def all_authors_list(request):
    authors = get_all_authors()
    template_response = loader.get_template('authors/all_authors.html')
    return HttpResponse(template_response.render({'authors': authors}, request))


def author_detail(request, author_id=1):
    print(author_id)
    selected_author = get_object_or_404(Author, pk=author_id)
    template_response = loader.get_template('authors/author_detail.html')
    return HttpResponse(template_response.render({'author': selected_author}, request))


def book_detail(request, book_id=1):
    selected_book = get_object_or_404(Book, pk=book_id)
    template_response = loader.get_template('books/book_detail.html')
    return HttpResponse(template_response.render({'book': selected_book}, request))


def showing_list_of_books(request):
    template_of_response = loader.get_template('books/list_all_books.html')
    books_objects = Book.objects.all()
    return HttpResponse(template_of_response.render({'list_of_books': books_objects}, request))
