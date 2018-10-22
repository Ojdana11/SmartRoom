from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Prints 'xD'"

    def handle(self, *args, **options):
        print ('xD')