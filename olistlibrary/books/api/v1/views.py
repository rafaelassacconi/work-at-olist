
from rest_framework import viewsets
from rest_framework import permissions
from books.models import Author, Book
from books.api.v1.serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """ Endpoint for Author list """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    """ Endpoint for Book list """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
