from django.urls import path, include

from SoftUniProjectMuscleArmy.articles.views import details_article, add_article, edit_article, delete_article

urlpatterns = [
    path('add/', add_article, name='add article'),
    path('article/<slug:article_slug>/', include([
        path('', details_article, name='details article'),
        path('edit/', edit_article, name='edit article'),
        path('delete/', delete_article, name='delete article'),
    ])),
]