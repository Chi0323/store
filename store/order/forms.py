from django import forms
from order.models import Order


class OrderForm(forms.ModelForm):
    payment=forms.fields.ChoiceField(
        choices=(('信用卡一次付清','信用卡一次付清'),('ATM付款','ATM付款'),('退貨/退款','退貨/退款'),('LINE PAY','LINE PAY'),('貨到付款','貨到付款')),
        required=True,
        label='付款類型',
        widget=forms.widgets.RadioSelect
        )
    fullName = forms.CharField(
        required=True,
        error_messages={
            "required": "收件人不能為空",
        },
        label='收件人', 
        widget=forms.TextInput(attrs={"class": "form-control2"})
        )
    telephone = forms.CharField(
        required=True,
        max_length=10,
        min_length=10,
        error_messages={
            "required": "手機號碼不能為空",
            "min_length": "手機號碼長度必須是10位",
            "max_length": "手機號碼長度必須是10位",
        },
        label='行動電話', 
        widget=forms.TextInput(attrs={"class": "form-control2"})
        )
    phone = forms.CharField(
        required=True,
        max_length=10,
        error_messages={
            "required": "市話不能為空",
            "max_length": "市話號碼長度必須是8位",
        },
        label='市話', 
        widget=forms.TextInput(attrs={"class": "form-control2"})
        )
    
    address = forms.CharField(
        required=True,
        max_length=128,
        error_messages={
            "required": "地址不能為空",
        },
        label='地址', 
        widget=forms.TextInput(attrs={"class": "form-control2"})
        )
    
    class Meta:
        model = Order
        fields = ['payment','fullName', 'telephone','phone','address']
        widgets ={'payment':forms.RadioSelect}