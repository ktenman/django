from django.shortcuts import render
from django.views import View

from books.models import Book, Author

def list_books(request):
    books = Book.objects.all()

    context = {
        'books': books,
    }

    return render(request, "list.html", context)

class AuthorList(View):
    def get(self , request):

        authors = Author.objects.all()

        context = {
            'authors': authors
        }

        return render(request, "authors.html", context)