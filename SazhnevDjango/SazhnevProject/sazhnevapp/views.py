from django.shortcuts import render
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


def log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'Выполнен вход по маршруту {func.__name__}')
        return result
    return wrapper


@log
def main(request):
    html_main = ("<html>\n<head>\n<title>Главная</title>\n</head>"
                 "\n<body>\n<h1>Домашняя страница!</h1>\n<div>\n"
                 "Добро пожаловать на нашу главную страницу! "
                 "Здесь вы найдете все необходимые информацию о нашей компании, наших услугах и продукции. "
                 "Мы стремимся предоставить вам лучший сервис и качественные товары, "
                 "чтобы удовлетворить все ваши потребности. "
                 "Наша команда профессионалов всегда готова помочь вам и ответить на все ваши вопросы."
                 "Спасибо, что выбрали нас!"
                 "\n</div>\n</body>\n</html>\n")
    return HttpResponse(html_main)


@log
def about_me(request):
    my_page = ("<html>\n<head>\n<title>О себе</title>\n</head>"
               "\n<body>\n<h1>Моя страница!</h1>\n<div>\n"
               "<i>Добро пожаловать на страницу обо мне! "
               "Я Сажнев Алексей и мне 33 года. "
               "Живу в Краснодарском крае и являюсь студентом GeekBrains."
               "Целеустремлён,общителен и творчески развит.</i>"
               "\n</div>\n</body>\n</html>\n")
    return HttpResponse(my_page)
