from django import forms
from .models import HardwareProduct

class ProductForm(forms.ModelForm):
    class Meta:
        model = HardwareProduct
        fields = ['name', 'type_product','stock', 'cost_price', 'selling_price']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name product', 'class': 'form-control-input'}),
            'stock': forms.NumberInput(attrs={'placeholder': 'Quantity in Stock', 'class': 'form-control-input'}),
            'cost_price': forms.NumberInput(attrs={'placeholder': 'Cust Price', 'class': 'form-control-input'}),
            'selling_price': forms.NumberInput(attrs={'placeholder': 'Selling Price', 'class': 'form-control-input'}),
            'type_product': forms.Select(attrs={'placeholder': 'Category', 'class': 'form-select-input'}),
        }
    