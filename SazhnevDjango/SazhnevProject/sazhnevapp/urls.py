from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about_me/', views.about_me, name='about_me'),
    path('catalog/', views.get_catalog, name='catalog'),
    path('orders/<int:client_id>/', views.get_orders, name='orders'),
]