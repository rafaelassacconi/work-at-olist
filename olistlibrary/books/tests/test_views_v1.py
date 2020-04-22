import os
import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Author, Book


class AuthorViewSetTest(APITestCase):
    """ Tests for authors API viewset """

    def setUp(self):
        folder = "%s/test_files/" % os.path.dirname(os.path.realpath(__file__))
        
        # Load authors
        authors = json.loads(open(folder+'authors.json', 'r').read())
        Author.objects.bulk_create([Author(name=item["name"]) for item in authors])

    def test_list_authors(self):
        """ Test list authors endpoint """
        url = reverse('author-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)["count"], Author.objects.count())

    def test_create_authors(self):
        """ Test create authors endpoint """
        url = reverse('author-list')
        name = 'Timothy Zahn'
        response = self.client.post(url, {'name': name})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 6)
        author_id = json.loads(response.content)["id"]
        self.assertEqual(Author.objects.get(id=author_id).name, name)

    def test_create_authors_no_data(self):
        """ Test create authors endpoint with no data """
        url = reverse('author-list')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_search_author_by_name(self):
        """ Test search author by name on list endpoint """
        url = reverse('author-list')
        response = self.client.get(url, {"name": "Stephen King"})
        result = json.loads(response.content)["results"][0]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result["name"], "Stephen King")
        self.assertEqual(result["id"], 3)

    def test_search_author_not_found(self):
        """ Test search author by name on list endpoint that not exists """
        url = reverse('author-list')
        response = self.client.get(url, {"name": "Stig Larsson"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)["count"], 0)

    def test_retrieve_author(self):
        """ Test retrieve author details endpoint """
        url = reverse('author-detail', kwargs={"pk": "1"})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)["name"], "Agatha Christie")

    def test_update_author(self):
        """ Test update author details endpoint with PUT """
        author_id = 1
        new_name = "Agatha Christie II"
        url = reverse('author-detail', kwargs={"pk": author_id})
        response = self.client.put(url, {"name": new_name})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)["name"], new_name)
        self.assertEqual(Author.objects.get(id=author_id).name, new_name)

    def test_delete_author(self):
        """ Test delete author details endpoint with DELETE """
        author_id = 1
        url = reverse('author-detail', kwargs={"pk": author_id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.count(), 4)

        with self.assertRaises(Author.DoesNotExist) as out:
            Author.objects.get(id=author_id)
        self.assertEqual('Author matching query does not exist.', str(out.exception))

    def test_delete_author_not_found(self):
        """ Test delete author details endpoint, that not exist, with DELETE """
        url = reverse('author-detail', kwargs={"pk": 18})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    

class BookViewSetTest(APITestCase):
    """ Tests for books API viewset """

    def setUp(self):
        folder = "%s/test_files/" % os.path.dirname(os.path.realpath(__file__))
        
        # Load authors
        authors = json.loads(open(folder+'authors.json', 'r').read())
        Author.objects.bulk_create([Author(name=item["name"]) for item in authors])

        # Load books
        books = json.loads(open(folder+'books.json', 'r').read())
        for b in books:
            book = Book.objects.create(
                name=b["name"],
                edition=b["edition"],
                publication_year=b["publication_year"],
            )
            book.authors.add(*b["authors"])

    def test_list_books(self):
        """ Test list books endpoint """
        url = reverse('book-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)["count"], Book.objects.count())

    def test_create_books(self):
        """ Test create books endpoint """
        url = reverse('book-list')
        name = 'Neuromancer'
        edition = 1
        year = 1984
        data = {
            "name": name,
            "edition": edition,
            "publication_year": year,
            "authors": [
                reverse('author-detail', kwargs={"pk": "3"}),
            ],
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 13)

        book = Book.objects.get(id=json.loads(response.content)["id"])
        self.assertEqual(book.name, name)
        self.assertEqual(book.edition, edition)
        self.assertEqual(book.publication_year, year)
        self.assertEqual(book.authors_name, "Stephen King")

    def test_create_books_no_data(self):
        """ Test create books endpoint with no data """
        url = reverse('book-list')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_search_book_by_name(self):
        """ Test search book by name on list endpoint """
        url = reverse('book-list')
        response = self.client.get(url, {"name": "Chronicle"})
        result = json.loads(response.content)["results"][0]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result["name"], "Chronicle")
        self.assertEqual(result["id"], 3)

    def test_search_book_not_found(self):
        """ Test search author by name on list endpoint that not exists """
        url = reverse('book-list')
        response = self.client.get(url, {"name": "Moby Dick"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)["count"], 0)

    def test_retrieve_book(self):
        """ Test retrieve book details endpoint """
        url = reverse('book-detail', kwargs={"pk": "1"})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)["name"], "Sorority Row")

    def test_update_book(self):
        """ Test update book details endpoint with PUT """
        book_id = 2
        new_name = "The Doctor II"
        url = reverse('book-detail', kwargs={"pk": book_id})
        data = {
            "name": new_name,
            "edition": 14,
            "publication_year": 2002,
            "authors": [
                reverse('author-detail', kwargs={"pk": "2"}),
                reverse('author-detail', kwargs={"pk": "4"})
            ],
        }
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)["name"], new_name)
        self.assertEqual(Book.objects.get(id=book_id).name, new_name)

    def test_delete_book(self):
        """ Test delete book details endpoint with DELETE """
        book_id = 1
        url = reverse('book-detail', kwargs={"pk": book_id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 11)

        with self.assertRaises(Book.DoesNotExist) as out:
            Book.objects.get(id=book_id)
        self.assertEqual('Book matching query does not exist.', str(out.exception))

    def test_delete_book_not_found(self):
        """ Test delete book details endpoint, that not exist, with DELETE """
        url = reverse('book-detail', kwargs={"pk": 32})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)