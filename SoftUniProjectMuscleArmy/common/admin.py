from django.contrib import admin

from SoftUniProjectMuscleArmy.common.models import ArticleComment


@admin.register(ArticleComment)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'publication_date_and_time', 'article')

