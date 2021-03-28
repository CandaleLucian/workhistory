from django import forms

from .models import SaleOrder


class SaleOrderModelForm(forms.ModelForm):
    class Meta:
        model = SaleOrder
        fields = [
            'client_name',
            'delivery_date',
            'product_description',
        ]

    # def clean_title # validations
