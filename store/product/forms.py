from django import forms
from product.models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(
        max_length=128,
        label='標題',        
        widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(
        label='內容', 
        widget=forms.Textarea(attrs={"class": "form-control"}))
    brand = forms.CharField(
        max_length=100,
        label='品牌', 
        widget=forms.TextInput(attrs={"class": "form-control"}))
    specifications = forms.CharField(
        max_length=100,
        label='規格', 
        widget=forms.TextInput(attrs={"class": "form-control"}))    
    price = forms.IntegerField(label='價格',
        widget=forms.NumberInput(attrs={"class": "form-control"}))
    quantity = forms.IntegerField(label='數量',
        widget=forms.NumberInput(attrs={"class": "form-control"}))
    

    class Meta:
        model = Product
        fields = '__all__'