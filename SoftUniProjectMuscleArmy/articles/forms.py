from django import forms

from SoftUniProjectMuscleArmy.articles.models import Article
from SoftUniProjectMuscleArmy.core.form_mixins import DisabledFormMixin


class ArticleBaseForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('slug', 'author')


class ArticleCreateForm(ArticleBaseForm):
    pass


class ArticleEditForm(ArticleBaseForm):
    pass


class ArticleDeleteForm(DisabledFormMixin, ArticleBaseForm):
    disabled_fields = ('title', 'description', 'content', 'article_photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            pass

        return self.instance

