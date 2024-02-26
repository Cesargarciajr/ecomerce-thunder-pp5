from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required = True

        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_display_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        