from SoftUniProjectMuscleArmy.products.models import Product


def get_product_by_slug(product_slug):
    return Product.objects.get(slug=product_slug)