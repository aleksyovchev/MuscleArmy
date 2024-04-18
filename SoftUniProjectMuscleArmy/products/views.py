from django.shortcuts import render

from SoftUniProjectMuscleArmy.products.models import Product
from SoftUniProjectMuscleArmy.products.utils import get_product_by_slug


def details_product(request, product_slug):
    product = get_product_by_slug(product_slug)
    products = Product.objects.all()
    i = 0
    random_products = []

    if len(products) < 4:
        random_products = [random_product for random_product in products if random_product != product]
    else:
        while i < 3:
            random_product = products.order_by('?').first()
            if random_product in random_products or product.name == random_product.name:
                pass
            else:
                random_products.append(random_product)
                i += 1

    context = {
        'product': product,
        'random_products': random_products,
    }

    return render(request, 'products/product-details-page.html', context)
