from django.shortcuts import render, redirect

from SoftUniProjectMuscleArmy.articles.forms import ArticleCreateForm, ArticleEditForm, ArticleDeleteForm
from SoftUniProjectMuscleArmy.articles.models import Article
from SoftUniProjectMuscleArmy.articles.utils import get_article_by_title
from SoftUniProjectMuscleArmy.common.forms import ArticleCommentForm
from SoftUniProjectMuscleArmy.common.models import ArticleComment, CommentLike
from SoftUniProjectMuscleArmy.core.comment_utils import apply_likes_count, apply_user_liked_comment


def details_article(request, article_slug):
    article = get_article_by_title(article_slug)
    comments = [apply_likes_count(comment) for comment in ArticleComment.objects.filter(article_id=article.pk)]
    comments = [apply_user_liked_comment(comment) for comment in comments]

    user_like_comments = []

    for comment in comments:
        user_like = CommentLike.objects.filter(comment_id=comment.id, user_id=request.user.pk)
        if user_like:
            user_like_comments.append(comment.id)

    context = {
        'comments': comments,
        'article': article,
        'comment_form': ArticleCommentForm(),
        'is_owner': article.author == request.user,
        'user_like_comments': user_like_comments
    }

    return render(request, 'articles/article-details-page.html', context)


def add_article(request):
    if request.method == 'GET':
        form = ArticleCreateForm()
    else:
        form = ArticleCreateForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('blog')

    context = {
        'form': form,
    }

    return render(request, 'articles/article-add-page.html', context)


def edit_article(request, article_slug):
    article = Article.objects.filter(slug=article_slug).get()
    if request.method == 'GET':
        form = ArticleEditForm(instance=article)
    else:
        form = ArticleEditForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('details article', article_slug=article_slug)

    context = {
        'form': form,
        'article_slug': article_slug,
    }

    return render(request, 'articles/article-edit-page.html', context)


def delete_article(request, article_slug):
    article = Article.objects.filter(slug=article_slug).get()

    if request.method == 'GET':
        form = ArticleDeleteForm(instance=article)
    else:
        form = ArticleDeleteForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('blog')

    context = {
        'form': form,
        'article_slug': article_slug,
    }
    return render(request, 'articles/article-delete-page.html', context)
