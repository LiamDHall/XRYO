from django import forms
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('album',)
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """Set display names to be displayed in form
        """

        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        display_names = [(c.id, c.get_display_name()) for c in categories]

        self.fields['category'].choices = display_names


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        exclude = ('date', 'product',)
        fields = '__all__'
