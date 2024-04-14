from django.urls import path

from SoftUniProjectMuscleArmy.common.views import index, blog, courses, like_comment, comment_article
from SoftUniProjectMuscleArmy.common.views import shop

urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('courses/', courses, name='courses'),
    path('shop/', shop, name='shop'),
    path('like/<int:comment_id>', like_comment, name='like comment'),
    path('articles/article/<int:article_id>', comment_article, name='comment article'),
]