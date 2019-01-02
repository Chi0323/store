from django import forms
from products.models import products


class productsForm(forms.ModelForm):
    title = forms.CharField(label='標題', max_length=128)
    content = forms.CharField(label='內容', widget=forms.Textarea)
    price = forms.IntegerField(label='價格', widget=forms.NumberInput())
    specifications = forms.CharField(label='規格', widget=forms.Textarea())
    quantity = forms.IntegerField(label='數量', widget=forms.NumberInput())

    class Meta:
        model = products
        fields = ['title', 'content','price','specifications','quantity']