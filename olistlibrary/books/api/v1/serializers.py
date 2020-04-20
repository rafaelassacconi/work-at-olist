from rest_framework import serializers
from books.models import Author, Book


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class BookSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Book
        fields = ['id', 'name', 'edition', 'publication_year']
