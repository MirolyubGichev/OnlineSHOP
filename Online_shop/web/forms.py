from django import forms as djangoForms

from Online_shop.web.models import Product


class ProductPostForm(djangoForms.ModelForm):
    class Meta:
        model= Product
        exclude = ['second_price']
        widgets = {
            'barcode' : djangoForms.TextInput(attrs={'class' : 'form-control'}),
            'name' : djangoForms.TextInput(attrs={'class' : 'form-control'}),
            # 'type' : djangoForms.TextInput(attrs={'class' : 'form-control'}),
            # 'category' : djangoForms.TextInput(attrs={'class' : 'form-control'}),
            'origin' : djangoForms.TextInput(attrs={'class' : 'form-control'}),
            'stock' : djangoForms.TextInput(attrs={'class' : 'form-control'}),
            'price' : djangoForms.TextInput(attrs={'class' : 'form-control'}),

        }







