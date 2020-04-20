# Olist Library API

This project is a fork from [Work at olist](https://github.com/olist/work-at-olist/) project by Olist. It's an application for a library to store book and authors data.

[Click here](https://afternoon-wave-72210.herokuapp.com/) to open a demo of the app on Heroku.

## 1. Versions

- Python 3.6.10
- Django 3.0.5
- Django Rest Framework 3.11.0


## 2. Links

- [Original instructions](https://github.com/rafaelassacconi/work-at-olist/blob/master/docs/INSTRUCTIONS.md)
- [API documentation](https://afternoon-wave-72210.herokuapp.com/v1/docs/)
- [Site adminitration](https://afternoon-wave-72210.herokuapp.com/admin/) (user: olist, pass: 0L1sTt3ch)
- Project activities on [Trello Kaban Board](https://trello.com/b/yCTzx50S/olist-library-api)


## 3. Modeling

Enhanced entity-relationship (EER) diagram:

![ERR Diagram](https://raw.githubusercontent.com/rafaelassacconi/work-at-olist/master/docs/database/err-diagram.png)


## 4. API Endpoints

Author endpoints, more information [here](https://afternoon-wave-72210.herokuapp.com/v1/docs/#authors).

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | /v1/authors/ | List all of authors |
| `POST` | /v1/authors/ | Creates a new author |
| `GET` | /v1/authors/{id}/ | Retrieves an author details |
| `PUT` | /v1/authors/{id}/ | Updates an author |
| `DELETE` | /v1/authors/{id}/ | Deletes an author |

Book endpoints, more information [here](https://afternoon-wave-72210.herokuapp.com/v1/docs/#books).

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | /v1/books/ | List all of books |
| `POST` | /v1/books/ | Creates a new book |
| `GET` | /v1/books/{id}/ | Retrieves a book details |
| `PUT` | /v1/books/{id}/ | Updates a book |
| `DELETE` | /v1/books/{id}/ | Deletes a book |

## 5. Running the project

Coming soon...
