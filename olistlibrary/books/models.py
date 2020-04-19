from django.db import models


class Author(models.Model):
    """ Authors model """
    name = models.CharField(max_length=250, db_index=True, 
        help_text="Complete name of the author.")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    """ Books model """
    name = models.CharField(max_length=250, db_index=True, 
        help_text="Book's title.")
    edition = models.PositiveSmallIntegerField(
        help_text="Number of book's edition.")
    publication_year = models.PositiveSmallIntegerField(db_index=True,
        help_text="Year of the publication date.")
    authors = models.ManyToManyField(Author, related_name='books',
        help_text="Book's authors, there may be more than one.")

    class Meta:
        ordering = ['-publication_year', 'name']

    def __str__(self):
        return '%s - %d ed.' % (self.name, self.edition)

    @property
    def authors_name(self):
        return ', '.join(self.authors.values_list('name', flat=True))