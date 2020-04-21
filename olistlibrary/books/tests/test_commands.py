import os
from datetime import datetime, timedelta
from django.test import TestCase
from django.core.management import call_command
from django.core.management.base import CommandError
from books.models import Author


class ImportAuthorsCommandTest(TestCase):
    """ Tests for import_authors command """

    def setUp(self):
        self.command = "import_authors"
        
        folder = "%s/test_files/" % os.path.dirname(os.path.realpath(__file__))

        self.file_simple = folder + "authors_simple.csv"
        self.file_wrong_column_name = folder + "authors_column.csv"
        self.file_huge = folder + "authors_huge.csv"
        
    def test_expected_simple_file(self):
        """ Call command with expected simple file """
        call_command(self.command, self.file_simple)
        self.assertEqual(Author.objects.count(), 3)

    def test_custom_column_name_file(self):
        """ Call command a custom column name in file """
        call_command(self.command, self.file_wrong_column_name, column_name="authors")
        self.assertEqual(Author.objects.count(), 5)

    def test_huge_file(self):
        """ Call command with a expected huge file """
        time_reference = timedelta(0, 60) # 1 min
        time_start = datetime.now()
        call_command(self.command, self.file_huge)
        time_end = datetime.now() - time_start
        self.assertEqual(Author.objects.count(), 2000000)
        self.assertLess(time_end, time_reference)

    def test_file_with_wrong_column_name(self):
        """ Call command with file but wrong name of column """
        with self.assertRaises(CommandError) as out:
            call_command(self.command, self.file_simple, column_name="foo")
        self.assertIn('Usecols do not match columns', str(out.exception))

    def test_file_not_found(self):
        """ Call command with file path that doesn't exists """
        with self.assertRaises(CommandError) as out:
            call_command(self.command, 'noexists.csv')
        self.assertIn('File not found', str(out.exception))

    def test_no_arguments(self):
        """ Call command with no arguments """
        with self.assertRaises(CommandError) as out:
            call_command(self.command)
        self.assertIn('the following arguments are required', str(out.exception))
