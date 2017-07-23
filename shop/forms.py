from __future__ import unicode_literals
from django import forms
from .models import Shop

class ShopModelForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'menu', 'rating','price']
        