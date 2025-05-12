
from django.contrib import admin

# Register your models here.
from .models import Customer, Menu, Restaurants
admin.site.register(Customer)
admin.site.register(Restaurants)
admin.site.register(Menu)