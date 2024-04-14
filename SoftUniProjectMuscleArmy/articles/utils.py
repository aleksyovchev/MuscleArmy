from SoftUniProjectMuscleArmy.articles.models import Article


def get_article_by_title(article_slug):
    return Article.objects.get(slug=article_slug)