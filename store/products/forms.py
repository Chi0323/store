from django import forms
from products.models import Products


class ProductsForm(forms.ModelForm):
    title = forms.CharField(label='標題', max_length=128)
    content = forms.CharField(label='內容', widget=forms.Textarea)
    specifications = forms.CharField(label='規格', max_length=128)
    price = forms.IntegerField(label='價格', widget=forms.NumberInput())
    quantity = forms.IntegerField(label='數量', widget=forms.NumberInput())

    class Meta:
        model = Products
        fields = ['title', 'content' ,'specifications','price','quantity']