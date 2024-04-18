from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from SoftUniProjectMuscleArmy.articles.validators import validate_file_less_than_5_mb
from SoftUniProjectMuscleArmy.core.model_mixins import StrFromFieldsMixin

UserModel = get_user_model()


class Article(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'title')
    MAX_TITLE = 100
    MAX_DESCRIPTION = 300

    title = models.CharField(
        max_length=MAX_TITLE,
        null=False,
        blank=False,
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION,
        null=False,
        blank=False,
    )

    content = models.CharField(
        null=False,
        blank=False,
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
    )

    article_photo = models.URLField(
        null=False,
        blank=True,
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

