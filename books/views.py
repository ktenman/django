from django.shortcuts import render
from books.models import Book

def list_books(request):
    books = Book.objects.all()

    context = {
        'books': books,
    }

    return render(request, "list.html", context)
