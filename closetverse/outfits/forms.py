from django import forms
from .models import Shirt, Pants, Shoes, Jacket, Accessories, Outfit

class ShirtForm(forms.ModelForm):
    class Meta:
        model = Shirt
        fields = ['brand', 'name', 'sku', 'size', 'color', 'picture']

class PantsForm(forms.ModelForm):
    class Meta:
        model = Pants
        fields = ['brand', 'name', 'sku', 'size', 'color', 'picture']

class ShoesForm(forms.ModelForm):
    class Meta:
        model = Shoes
        fields = ['brand', 'name', 'sku', 'size', 'color', 'picture']

class JacketForm(forms.ModelForm):
    class Meta:
        model = Jacket
        fields = ['brand', 'name', 'sku', 'size', 'color', 'picture']

class AccessoriesForm(forms.ModelForm):
    class Meta:
        model = Accessories
        fields = ['brand', 'name', 'sku', 'size', 'color', 'picture']

class OutfitForm(forms.ModelForm):
    class Meta:
        model = Outfit
        fields = ['shirt', 'pants', 'shoes', 'jacket', 'accessories']
        widgets = {
            'accessories': forms.CheckboxSelectMultiple(),
        }