from django.contrib import admin
from .models import ContactUser, SubscribeUser, Category, Product
from django.db import models
from django.conf import settings

class ContactUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

class SubscribeUserAdmin(admin.ModelAdmin):
    list_display = ('email',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'image')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(ContactUser, ContactUserAdmin)
admin.site.register(SubscribeUser, SubscribeUserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
