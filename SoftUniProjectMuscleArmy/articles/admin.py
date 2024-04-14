from django.contrib import admin

from SoftUniProjectMuscleArmy.articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author', 'created_at')
