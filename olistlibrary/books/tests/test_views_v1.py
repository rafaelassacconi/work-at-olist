import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Author, Book


class AuthorViewSetTest(APITestCase):
    """ 
        Tests for authors API viewset 
        For reference: https://www.django-rest-framework.org/api-guide/status-codes/
    """

    def setUp(self):
        authors = [
            "Agatha Christie",
            "William Shakespeare",
            "Stephen King",
            "Paulo Coelho",
            "Louis L'Amour",
        ]
        Author.objects.bulk_create([Author(name=name) for name in authors])

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
    