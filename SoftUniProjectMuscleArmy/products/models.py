from django.db import models
from django.utils.text import slugify

from SoftUniProjectMuscleArmy.core.model_mixins import StrFromFieldsMixin


class Product(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'name')
    MAX_NAME = 30
    MAX_DESCRIPTION = 100
    MAX_PRICE = 10
    MAX_SIZE = 3

    name = models.CharField(
        max_length=MAX_NAME,
        null=False,
        blank=False,
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION,
        null=False,
        blank=False,
    )

    price = models.CharField(
        max_length=MAX_PRICE,
        null=False,
        blank=False,
    )

    old_price = models.CharField(
        max_length=MAX_PRICE,
        null=True,
        blank=True,
    )

    size = models.CharField(
        max_length=MAX_SIZE,
        null=False,
        blank=False,
    )

    product_photo = models.URLField(
        null=False,
        blank=False,
    )

    type = models.CharField(
        choices=[('Clothes', 'Clothes'), ('Equipment', 'Equipment'), ('Supplements', 'Supplements')],
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')

        return super().save(*args, **kwargs)
