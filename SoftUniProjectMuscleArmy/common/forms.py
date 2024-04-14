from django import forms

from SoftUniProjectMuscleArmy.common.models import ArticleComment


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ('text',)
        labels = {
            'text': ''
        }
        widgets = {
            'text': forms.Textarea(attrs={'cols': 40, 'rows': 40, 'placeholder': 'Добави коментар...'}),
        }