# Generated by Django 5.0.2 on 2024-03-07 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sazhnevapp', '0004_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(blank=True, to='sazhnevapp.product'),
        ),
    ]
