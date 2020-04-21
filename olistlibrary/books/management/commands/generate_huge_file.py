import os
import csv
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Generates a huge file with authors to test"

    def handle(self, *args, **options):
        # Set the number of rows here:
        rows = 2000000
        
        # The file will be generate in here:
        file_path = 'olistlibrary/books/tests/test_files/authors_huge.csv'

        with open(file_path, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['name'])

            n = 0
            while n < rows:
                writer.writerow(['JustABigFirstname WithABigLastname'])
                n += 1

        print("Finished! %d in %dMB file." % (rows, os.path.getsize(file_path)/(1024*1024)))
