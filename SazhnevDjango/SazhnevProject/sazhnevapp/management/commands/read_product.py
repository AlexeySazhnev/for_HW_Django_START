from django.core.management.base import BaseCommand
from sazhnevapp.models import Product


class Command(BaseCommand):
    help = "Read product."

    def add_arguments(self, parser):
        parser.add_argument('pk')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        product = Product.objects.filter(pk=pk).first()
        self.stdout.write(f'{product}')