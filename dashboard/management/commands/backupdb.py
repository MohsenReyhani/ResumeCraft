import os
import datetime
from django.core.management.base import BaseCommand
from django.conf import settings
from django.core import management

class Command(BaseCommand):
    help = 'Backup the database'

    def handle(self, *args, **kwargs):
        backup_dir = os.path.join(settings.BASE_DIR, 'backups')
        os.makedirs(backup_dir, exist_ok=True)
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = os.path.join(backup_dir, f'db_backup_{timestamp}.json')

        self.stdout.write(f'Backing up database to {backup_file}')
        with open(backup_file, 'w') as f:
            management.call_command('dumpdata', stdout=f)
        self.stdout.write(self.style.SUCCESS(f'Successfully backed up database to {backup_file}'))
