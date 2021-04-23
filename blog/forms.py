from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('date',)
        fields = ('title', 'image', 'article')

    article = forms.CharField(
        widget=forms.Textarea(
            attrs={"rows": 5, "cols": 20}
        )
    )
