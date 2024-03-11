from django.contrib import admin
from .models import Client, Product, Order
# Register your models here.
@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'registration_date']
    list_filter = ['registration_date']
    ordering = ['name']
    search_fields = ['id']
    search_help_text = 'Поиск по полю id клиента (Введите id)'
    list_editable = ['email']
    list_per_page = 10
    readonly_fields = ['registration_date']
    fieldsets = [
        (
          'Имя',
          {
              'fields': ['name'],
              'classes': ['wide'],
          },
        ),
        (
           'Контакты',
           {
               'fields': ['phone', 'email', 'address'],
               'classes': ['collapse'],
           }
        ),
        (
            'Дата регистрации',
            {
                'fields': ['registration_date'],
            },
        ),
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['phone'].widget.attrs['style'] = 'width: 30%;'  # Установка ширины поля "phone"
        return form
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'quantity','added_date']
    list_filter = ['added_date']
    ordering = ['name']
    search_fields = ['name']
    search_help_text = 'Поиск по названию продукта'
    list_editable = ['quantity', 'price']
    list_per_page = 5
    readonly_fields = ['added_date']
    fieldsets = [
        (
            'Имя и Описание',
            {
                'fields': ['name', 'description', 'image'],
                'classes': ['wide'],
            },
        ),
        (
            'Учёт',
            {
                'fields': ['price', 'quantity', 'added_date'],
            },
        ),
    ]

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ['id', 'client', 'total_amount', 'order_date']
    list_filter = ['order_date']
    ordering = ['client']
    search_fields = ['id']
    search_help_text = 'Поиск по id заказа'
    list_per_page = 5
    readonly_fields = ['order_date']
    fieldsets = [
        (
            'Заказчик',
            {
                'fields': ['client'],
                'classes': ['wide'],
            },
        ),
        (
            'Заказанные продукты',
            {
                'fields': ['products'],
                'classes': ['wide'],
            },
        ),
        (
            'Время и сумма заказа',
            {
                'fields': ['total_amount', 'order_date'],
                'classes': ['collapse'],
            },
        ),
    ]
