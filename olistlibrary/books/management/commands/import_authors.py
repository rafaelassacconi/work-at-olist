import os
from datetime import datetime
from pandas import read_csv
from django.core.management.base import BaseCommand, CommandError
from books.models import Author


class Command(BaseCommand):
    help = "Import authors from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", 
            type=str, help="CSV complete file path")
        parser.add_argument("-colname", "--column-name", 
            type=str, default="name", help="Name of the column")

    def handle(self, *args, **options):
        time_start = datetime.now()

        # Get parameters
        path = options.get("csv_file", "")
        colname = options.get("column_name", "name")

        # Check if file exists
        if not path or not os.path.exists(path):
            raise CommandError("File not found: %s" % path)
        
        # Read file
        try:
            content = read_csv(
                path, 
                usecols=[colname], 
                skip_blank_lines=True, 
                chunksize=1000000
            )
        except Exception as e:
            raise CommandError("Error reading the file: %s" % str(e))

        # Import authors
        imported = 0
        for chunk in content:
            values = chunk.to_dict()[colname].values()
            Author.objects.bulk_create([Author(name=name) for name in values])
            imported += chunk.size
            print(imported, 'imported')

        time_end = datetime.now() - time_start
        print("Finished! %d authors successfully imported. Time: %s" % (imported, str(time_end)))
