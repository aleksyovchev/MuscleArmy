from django.contrib.auth import get_user_model
from django.db import models

from SoftUniProjectMuscleArmy.articles.models import Article

UserModel = get_user_model()


class ArticleComment(models.Model):
    MAX_TEXT_LENGTH = 300

    text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True,
    )

    article = models.ForeignKey(
        Article,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )


class CommentLike(models.Model):
    comment = models.ForeignKey(
        ArticleComment,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )