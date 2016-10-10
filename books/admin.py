from django.contrib import admin
from .models import Author, Book

class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ('About Book', {'fields': ['title', 'authors']}),
        ('Comment', {'fields': ['is_bookmarked', 'comment', 'date_commented']}),
    ]

    readonly_fields = ('date_commented',)

    def book_authors(self, obj):
        return obj.list_authors()

    book_authors.short_description = 'Author(s)'

    list_display = ('title', 'book_authors', 'date_commented', 'is_bookmarked',)
    list_editable = ('is_bookmarked',)
    list_display_links = ('title', 'book_authors', 'date_commented',)
    list_filter = ('is_bookmarked',)
    search_fields = ['title', 'authors__name', ]

# Register your models here.
admin.site.register(Author)
admin.site.register(Book, BookAdmin)