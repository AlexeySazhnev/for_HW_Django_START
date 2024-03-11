from django.core.management.base import BaseCommand
from sazhnevapp.models import Order, Product, Client

class Command(BaseCommand):
    help = "Create order."

    def handle(self, *args, **kwargs):
        client_id = int(input("Введите ID клиента: "))

        try:
            client = Client.objects.get(pk=client_id)
        except Client.DoesNotExist:
            self.stdout.write(self.style.ERROR("Клиент с указанным ID не существует"))
            return

        products = Product.objects.all()
        print("Доступные товары:")
        for product in products:
            print(f"{product.id}. {product.name} - {product.description} - Цена: {product.price}")

        product_ids = input("Введите ID выбранных товаров (через запятую): ")
        product_ids = [int(pid) for pid in product_ids.split(',')]

        order_total_amount = 0
        selected_products = []
        for pid in product_ids:
            product = Product.objects.get(id=pid)
            selected_products.append(product)
            order_total_amount += product.price

        order = Order.objects.create(
            client=client,
            total_amount=order_total_amount
        )
        order.products.set(selected_products)

        self.stdout.write(self.style.SUCCESS(f'Заказ успешно создан для {client.name}'))
