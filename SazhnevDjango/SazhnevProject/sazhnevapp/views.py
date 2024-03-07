from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Product, Client, Order
from .forms import ProductForm
import pandas as pd
import logging

logger = logging.getLogger(__name__)


def log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'Выполнен вход по маршруту {func.__name__}')
        return result

    return wrapper


def get_html_table(data):
    table = []
    for el in data:
        table.append(
            {"Позиция товара (id)": el.id,
             "Имя товара": el.name,
             "Описание": el.description,
             "Количество": el.quantity,
             "Цена": el.price,
             "Дата завоза": el.added_date,
             "Фото продукта": el.image,
             }
        )
    return pd.DataFrame(table).to_html(index=False)


@log
def main(request):
    return render(request, "base.html")


@log
def about_me(request):
    my_page = ("<html>\n<head>\n<title>О нас</title>\n</head>"
               "\n<body>\n<h1>О нас!</h1>\n<div>\n"
               "<i>Мы - команда людей, которые любят заботиться о своем здоровье и здоровье своих клиентов. "
               "Наш интернет магазин 'Овощи и фрукты' был создан с целью "
               "предоставить качественные и свежие продукты прямо к вашему столу.</p>"
               "<p>Мы работаем напрямую с производителями, чтобы обеспечить наших клиентов только лучшими овощами и фруктами."
               "Мы следим за качеством продукции и стремимся предложить широкий ассортимент товаров для разнообразия вашего стола.</p>"
               "<p>Наша цель - сделать вашу жизнь здоровее и легче, предлагая качественные продукты, удобный сервис доставки и отличное обслуживание.</p>"
               "<p>Присоединяйтесь к нашему магазину 'Овощи и фрукты'"
               "и наслаждайтесь свежими и вкусными продуктами каждый день!</p></i>"
               "\n</div>\n</body>\n</html>\n")
    return HttpResponse(my_page)


def get_catalog(request):
    product = Product.objects.all()
    result = get_html_table(product)
    return render(request, 'sazhnevapp/catalog.html', {'table': result})


def get_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    """Заказы за неделю"""
    weekly_orders = Order.objects.filter(client=client,
                                         order_date__gte=datetime.now() - timedelta(days=7)).order_by('order_date')
    """Заказы за месяц"""
    monthly_orders = Order.objects.filter(client=client,
                                          order_date__gte=datetime.now() - timedelta(days=30)).order_by('order_date')
    """Заказы за год"""
    orders_per_year = Order.objects.filter(client=client,
                                           order_date__gte=datetime.now() - timedelta(days=365)).order_by('order_date')
    return render(request, "sazhnevapp/orders.html", {'client': client,
                                                      'weekly_orders': weekly_orders,
                                                      'monthly_orders': monthly_orders,
                                                      'orders_per_year': orders_per_year}
                  )


def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = ProductForm(instance=product)
    return render(request, 'sazhnevapp/edit_product.html', {'form': form})
