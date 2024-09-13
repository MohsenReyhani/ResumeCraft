from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings

class Command(BaseCommand):
    help = 'Run makemigrations for all installed apps'

    def handle(self, *args, **kwargs):
        # Get all installed apps from settings
        installed_apps = settings.INSTALLED_APPS

        # Exclude Django's built-in apps or third-party apps if needed
        exclude_apps = ['django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 
                        'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles']

        # Filter out excluded apps, keep only apps that are relevant for migrations
        apps_to_migrate = [app for app in installed_apps if app not in exclude_apps]

        # Run makemigrations for each app
        for app in apps_to_migrate:
            self.stdout.write(self.style.SUCCESS(f'Running makemigrations for {app}...'))
            call_command('makemigrations', app)

        # Run migrate after makemigrations
        self.stdout.write(self.style.SUCCESS('Running migrate...'))
        call_command('migrate')

        self.stdout.write(self.style.SUCCESS('Finished running makemigrations and migrate.'))
