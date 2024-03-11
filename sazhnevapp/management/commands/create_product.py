from django.core.management.base import BaseCommand
from sazhnevapp.models import Product


class Command(BaseCommand):
    help = "Create product."

    def add_arguments(self, parser):
        parser.add_argument('name')
        parser.add_argument('description')
        parser.add_argument('price')
        parser.add_argument('quantity')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        description = kwargs['description']
        price = kwargs['price']
        quantity = kwargs['quantity']
        product = Product.objects.create(
            name=name,
            description=description,
            price=price,
            quantity=quantity
        )
        self.stdout.write(f'{product}')
