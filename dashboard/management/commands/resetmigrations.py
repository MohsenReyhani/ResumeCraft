from django.core.management.base import BaseCommand
import os
import shutil

class Command(BaseCommand):
    help = 'Removes all migrations, the SQLite database, and __pycache__ directories'

    def handle(self, *args, **kwargs):
        # Get the current directory
        current_directory = os.getcwd()

        # Delete the SQLite database
        if os.path.exists(os.path.join(current_directory, 'db.sqlite3')):
            os.remove(os.path.join(current_directory, 'db.sqlite3'))


        # Collect all migration files and __pycache__ directories to delete
        paths_to_delete = []

        for root, dirs, files in os.walk(current_directory):
            for file in files:
                if file == '0001_initial.py':
                    paths_to_delete.append(os.path.dirname(os.path.join(root, file)))
            for dir in dirs:
                if dir == '__pycache__':
                    paths_to_delete.append(os.path.join(root, dir))

        # Delete the collected paths
        for path in paths_to_delete:
            if os.path.exists(path):
                shutil.rmtree(path)

        self.stdout.write(self.style.SUCCESS('Successfully reset migrations, deleted the SQLite database, and removed __pycache__ directories.'))
