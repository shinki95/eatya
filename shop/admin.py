from django.contrib import admin
from .models import Shop


class ShopAdmin(admin.ModelAdmin):
     list_dispaly = ['id', 'menu', 'price', 'updated_at']
admin.site.register(Shop, ShopAdmin)