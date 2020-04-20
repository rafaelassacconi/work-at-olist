
from rest_framework import viewsets
from rest_framework import permissions
from books.models import Author, Book
from books.api.v1.serializers import AuthorSerializer, BookSerializer
from django_filters.rest_framework import DjangoFilterBackend


class AuthorViewSet(viewsets.ModelViewSet):
    """ Endpoints for Author list """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class BookViewSet(viewsets.ModelViewSet):
    """ Endpoints for Book list """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'edition', 'publication_year', 'authors__name']