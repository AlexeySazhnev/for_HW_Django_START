from django.core.management.base import BaseCommand
from sazhnevapp.models import Product


class Command(BaseCommand):
    help = "Delete product."

    def add_arguments(self, parser):
        parser.add_argument('pk')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            product.delete()
        self.stdout.write(f'{product}')
