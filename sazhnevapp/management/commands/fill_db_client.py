import random
from django.core.management.base import BaseCommand
from sazhnevapp.models import Client

CLIENTS = "Александр", "Сергей", "Елена", "Степан", "Наталья", "Дарья","Олег" ,"Виктория"
DATA = "2024-01-14", "2023-05-07", "2022-03-04"


class Command(BaseCommand):
    help = "Filling in fake data in the database."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for _ in range(1, count + 1):
            name_client = random.choice(CLIENTS)
            registration_date = random.choice(DATA)
            phone = random.randint(1111111111, 9999999999)
            if name_client == "Александр" and "Наталья":
                address = "Краснодар"
            elif name_client == "Сергей" and "Олег":
                address = "Ростов"
            elif name_client == "Виктория" and "Степан":
                address = "Сочи"
            else:
                address="Москва"
            client = Client(name=name_client,
                            email=f'{name_client}@mail.ru',
                            address=address,
                            phone=phone,
                            registration_date=registration_date)
            client.save()
