# Olist Library API

This project is a fork from [Work at olist](https://github.com/olist/work-at-olist/) project by Olist. It's an application for a library to store book and authors data.

[Click here](https://afternoon-wave-72210.herokuapp.com/) to open a demo of the app on Heroku.

## 1. Versions

- Ubuntu 18.04.3
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

### 5.1 Virtualenv

Install pip, virtualenv and virtualenvwrapper packages:
```
sudo apt-get install python3-pip
sudo pip3 install virtualenv virtualenvwrapper
```
For configure the VirtualEnvWrapper, edit the file `/home/user/.bashrc`:
Include the content bellow at the end of the file:
```
# Python Virtualenvs 
export WORKON_HOME=/home/user/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.6
source /usr/local/bin/virtualenvwrapper.sh 
export PIP_REQUIRE_VIRTUALENV=true 
```
Restart the terminal and run the command bellow to create a virtualenv:
```
mkvirtualenv olistlibrary
```

### 5.2 Prepare the project
Clone this repository and access to the folder:
```
git clone https://github.com/rafaelassacconi/work-at-olist.git
```
Activate the virtualenv:
```
workon olistlibrary
```
Install the packages required:
```
pip install -r requirements.txt
```
Run migrate command to create a database:
```
olistlibrary/manage.py migrate
```
Run the command bellow to import authors data:
```
olistlibrary/manage.py import_authors files/authors.csv
```
### 5.3 Run the local application
Use the command bellow to execute the application:
```
olistlibrary/manage.py runserver
```
Access the application using this link: [http://localhost:8000](http://localhost:8000)

### 5.4 Tests
If you want run the tests, use this command bellow:
```
olistlibrary/manage.py test books
```