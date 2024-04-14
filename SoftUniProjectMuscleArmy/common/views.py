from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from SoftUniProjectMuscleArmy.articles.models import Article
from SoftUniProjectMuscleArmy.common.forms import ArticleCommentForm
from SoftUniProjectMuscleArmy.common.models import CommentLike
from SoftUniProjectMuscleArmy.courses.models import Course
from SoftUniProjectMuscleArmy.products.models import Product


def index(request):
    context = {
        'products': Product.objects.all(),
    }

    return render(request, 'common/home-page.html', context)


def blog(request):
    context = {
        'articles': Article.objects.all(),
    }

    return render(
        request,
        'common/blog-page.html',
        context,
    )


def shop(request):
    context = {
        'products': Product.objects.all(),
    }

    return render(request, 'products/shop-page.html', context)


def courses(request):
    context = {
        'courses': Course.objects.all(),
    }

    return render(request, 'common/courses-page.html', context)


@login_required
def like_comment(request, comment_id):
    user_liked_comments = CommentLike.objects.filter(comment_id=comment_id, user_id=request.user.pk)

    if user_liked_comments:
        user_liked_comments.delete()
    else:
        CommentLike.objects.create(
            comment_id=comment_id,
            user_id=request.user.pk
        )

    return redirect(request.META['HTTP_REFERER'] + f'#comment-{comment_id}')


def comment_article(request, article_id):
    article = Article.objects.filter(pk=article_id).get()

    form = ArticleCommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()

    return redirect(request.META['HTTP_REFERER'])