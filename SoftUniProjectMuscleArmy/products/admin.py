from django.contrib import admin

from SoftUniProjectMuscleArmy.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'old_price', 'size')

