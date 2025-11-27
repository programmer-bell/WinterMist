from django import forms

from .models import Product

# Form for take data from the client

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price'
        ]


