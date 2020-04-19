from django.contrib import admin
from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'books_qty')
    search_fields = ('name',)

    def books_qty(self, author):
        return author.books.count()
    books_qty.short_description = 'Books'


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'authors_name', 'edition', 'publication_year')
    list_filter = ('publication_year',)
    search_fields = ('name', 'authors__name')

