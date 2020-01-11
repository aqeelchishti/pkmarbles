from django.db import models

class ContactUser(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=120)
    message = models.TextField(max_length=240)

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return "/contact/"

class SubscribeUser(models.Model):
    email = models.EmailField(max_length=120)

    def __str__(self):
        return '{}'.format(self.email)

    def get_absolute_url(self):
        return "/"

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return '{}'.format(self.name)

class Product(models.Model):
    name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField(max_length=200, null=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return '{}'.format(self.name)
