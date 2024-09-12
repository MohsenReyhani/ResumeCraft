from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'create simple user'

    def handle(self, *args, **kwargs):
        User = get_user_model()  # get the custom user model
        if not User.objects.filter(phone_no='09300000000').exists():
            User.objects.create_superuser('09300000000', 'ass')
            self.stdout.write(self.style.SUCCESS('User 09300000000 added.'))
        else:
            self.stdout.write(self.style.SUCCESS('User 09300000000 already exsists.'))