from django.db import models
# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    registration_date = models.DateField(auto_now_add=True)
    products = models.ManyToManyField('Product', related_name='clients')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, {self.description}, {self.quantity}"


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Order for {self.client.name}'
