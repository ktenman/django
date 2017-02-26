from django.shortcuts import render
from django.views import View
from books.models import Book, Author
from django.db.models import Count


def list_books(request):
    books = Book.objects.all()

    context = {
        'books': books,
    }

    return render(request, "list.html", context)


class AuthorList(View):
    @staticmethod
    def get(request):
        authors = Author.objects.annotate(
            published_books=Count('books')
        ).filter(
            published_books__gt=0
        )

        context = {
            'authors': authors
        }

        return render(request, "authors.html", context)
