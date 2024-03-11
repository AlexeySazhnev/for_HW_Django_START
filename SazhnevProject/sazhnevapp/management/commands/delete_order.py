from django.core.management.base import BaseCommand
from sazhnevapp.models import Order

class Command(BaseCommand):
    help = 'Delete all order from the database'

    def add_arguments(self, parser):
        parser.add_argument('pk')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        if order is not None:
            order.delete()
        self.stdout.write(f'{order}')