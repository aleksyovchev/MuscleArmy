from django.db import models
from django.utils.text import slugify


class Course(models.Model):
    title = models.CharField(
        null=False,
        blank=False,
    )

    duration = models.IntegerField(
        null=False,
        blank=False,
    )

    length_per_day = models.IntegerField(
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
            self.slug = slugify(f'{self.id}-{self.title}')

        return super().save(*args, **kwargs)
