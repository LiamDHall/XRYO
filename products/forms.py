from django import forms
from .models import Product, Variant, Category


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
