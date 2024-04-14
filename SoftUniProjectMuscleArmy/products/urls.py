from django.urls import path, include

from SoftUniProjectMuscleArmy.products.views import details_product

urlpatterns = [
    path('products/<slug:product_slug>', include([
        path('', details_product, name='details product'),
    ])),
]