from django.core.management.base import BaseCommand
from sazhnevapp.models import Order

class Command(BaseCommand):
    help = 'Delete all order from the database'

    def handle(self, *args, **options):
        Order.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('All orders have been deleted from the database'))
