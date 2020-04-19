from django.test import TestCase
from django.db.utils import IntegrityError
from books.models import Author, Book


class AuthorModelTest(TestCase):
    """ Tests for Author model """

    def test_author_creation(self):
        """ Test a simple creation of an author object """
        name = 'Robin Cook'
        author = Author.objects.create(name=name)
        self.assertEqual(author.name, name)

    def test_author_creation_with_no_name(self):
        """ Test if name field is required """
        self.assertRaises(IntegrityError, Author.objects.create, 
            name=None
        )


class BookModelTest(TestCase):
    """ Tests for Book model """

    def test_book_creation(self):
        """ Test a simple creation of a book object """
        name = 'Terminal'
        edition = 1
        year = 1992
        authors = []

        book = Book.objects.create(
            name = name,
            edition = edition,
            publication_year = year,
        )

        self.assertEqual(book.name, name)
        self.assertEqual(book.edition, edition)
        self.assertEqual(book.publication_year, year)
        self.assertEqual(book.authors.count(), 0)

        # Add authors
        book.authors.add(Author.objects.create(name='Robin Cook'))
        book.authors.add(Author.objects.create(name='Ivan Gregory'))
        self.assertEqual(book.authors.count(), 2)


    def test_book_creation_with_no_name(self):
        """ Test if name field is required """
        self.assertRaises(IntegrityError, Book.objects.create, 
            name=None, 
            edition=1, 
            publication_year=1992
        )

    def test_book_creation_with_no_edition(self):
        """ Test if edition field is required """
        self.assertRaises(IntegrityError, Book.objects.create, 
            name='Terminal', 
            edition=None, 
            publication_year=1992
        )

    def test_book_creation_with_no_year(self):
        """ Test if publication_year field is required """
        self.assertRaises(IntegrityError, Book.objects.create, 
            name='Terminal', 
            edition=1, 
            publication_year=None
        )
