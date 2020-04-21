import os
from pandas import read_csv
from random import randint
from django.core.management.base import BaseCommand, CommandError
from books.models import Author, Book


class Command(BaseCommand):
    help = "Import books from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="CSV complete file path")

    def handle(self, *args, **options):
        # Get parameters
        path = options.get("csv_file", "")

        # Check if file exists
        if not path or not os.path.exists(path):
            raise CommandError("File not found: %s" % path)
        
        # Read file
        try:
            content = read_csv(
                path, 
                usecols=['name', 'edition', 'year'], 
                skip_blank_lines=True,
            )
        except Exception as e:
            raise CommandError("Error reading the file: %s" % str(e))
        
        # Import books
        total_authors = Author.objects.count()

        for _, name, edition, year in content.to_records():

            # Import book data
            book = Book.objects.create(
                name = name,
                edition = edition,
                publication_year = year,
            )
            
            # Set random authors per book
            for n in range(randint(1, 2)):
                book.authors.add(randint(1, total_authors))

        print("Finished! %d books successfully imported." % content.size)
