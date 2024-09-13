from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
	help = 'Run makemigrations for specific apps'

	def add_arguments(self, parser):
		# Add a new '--message' argument
		parser.add_argument(
			'--ignorestuff',
			action='store_true',  # This means the flag is a boolean switch
			help='Use removestuff mode',
		)

	def handle(self, *args, **kwargs):

		ignore_stuff = kwargs.get('ignorestuff')
		
		self.stdout.write(self.style.SUCCESS('Starting ...'))
		call_command('resetmigrations')
		call_command('runmigrations')
		call_command('createuser')

		self.stdout.write(self.style.SUCCESS('Finished All.'))