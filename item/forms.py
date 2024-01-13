from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image', 'currency')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category'].label = 'Category:'
        self.fields['category'].widget.attrs.update({'class': 'category-class'})

        self.fields['name'].label = 'Item Name:'
        self.fields['name'].widget.attrs.update({'class': 'name-class'})

        self.fields['description'].label = 'Description:'
        self.fields['description'].widget.attrs.update({'class': 'description-class'})

        self.fields['price'].label = 'Price:'
        self.fields['price'].widget.attrs.update({'class': 'price-class'})

        self.fields['image'].label = 'Upload image:'
        self.fields['image'].widget.attrs.update({'class': 'image-class'})

        self.fields['currency'].widget.attrs.update({'class': 'currency-class'})
        self.fields['currency'].widget = forms.RadioSelect(choices=[('USD', '$'), ('GEL', '₾')])


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image', 'currency', 'is_sold')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category'].label = 'Category:'
        self.fields['category'].widget.attrs.update({'class': 'category-class'})

        self.fields['name'].label = 'Item Name:'
        self.fields['name'].widget.attrs.update({'class': 'name-class'})

        self.fields['description'].label = 'Description:'
        self.fields['description'].widget.attrs.update({'class': 'description-class'})

        self.fields['price'].label = 'Price:'
        self.fields['price'].widget.attrs.update({'class': 'price-class'})

        self.fields['image'].label = 'Upload image:'
        self.fields['image'].widget.attrs.update({'class': 'image-class'})

        self.fields['currency'].widget.attrs.update({'class': 'currency-class'})
        self.fields['currency'].widget = forms.RadioSelect(choices=[('USD', '$'), ('GEL', '₾')])

        self.fields['is_sold'].label = 'Sold:'
        self.fields['is_sold'].widget.attrs.update({'class': 'image-class'})

