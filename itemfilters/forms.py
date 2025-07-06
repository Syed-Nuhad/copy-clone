from django import forms
from .models import Filter

class FilterForm(forms.ModelForm):
    class Meta:
        model = Filter
        fields = ['category', 'subcategory', 'keywords', 'min_price', 'max_price', 'autocop_enabled']
