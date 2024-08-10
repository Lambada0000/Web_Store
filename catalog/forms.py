from django.forms import ModelForm
from .models import Product, Version


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'photo', 'category', 'price')


class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
