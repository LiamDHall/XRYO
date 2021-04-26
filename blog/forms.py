from django import forms
from .models import Post
from .widgets import CustomImageInput


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('date',)
        fields = ('title', 'image', 'article')

    image = forms.ImageField(label='Post Image', widget=CustomImageInput)

    article = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'cols': 20}
        )
    )

    def __init__(self, *args, **kwargs):
        """Set form styling class
        """

        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-input'
