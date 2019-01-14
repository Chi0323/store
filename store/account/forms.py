from django import forms
from account.models import User
from random import choices

class UserForm(forms.ModelForm):
    username = forms.CharField(
        required=True,
        min_length=6,
        max_length=15,
        error_messages={
            "required": "用户名不能為空",
            "min_length": "用户名長度不能小於6", 
            "max_length": "用户名長度不能小於15"
        },
        label='', 
        widget=forms.TextInput(attrs={"placeholder": "帳號", "class": "form-control"})
        )
    password = forms.CharField(
        required=True,
        min_length=6,
        max_length=30,
        error_messages={
            "required": "密碼不能為空",
            "min_length": "密碼長度不能小於6",
            "max_length": "用户名長度不能超過30",
        },
        label='', 
        widget=forms.PasswordInput(attrs={"placeholder": "請輸入密碼", "class": "form-control"})
        )
    password2 = forms.CharField(
        required=True,
        min_length=6,
        max_length=30,
        error_messages={
            "required": "密碼不能為空",
            "min_length": "密碼長度不能小於6",
            "max_length": "用户名長度不能超過30",
        },
        label='', 
        widget=forms.PasswordInput(attrs={"placeholder": "再次輸入密碼", "class": "form-control"})
        )
    fullName = forms.CharField(
        required=True,
        error_messages={
            "required": "姓名不能為空",
        },
        label='', 
        widget=forms.TextInput(attrs={"placeholder": "姓名", "class": "form-control"})
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
        label='', 
        widget=forms.TextInput(attrs={"placeholder": "電話", "class": "form-control"})
        )
    birthday = forms.DateField(
        required=True,
        label='', 
        widget=forms.TextInput(attrs={"placeholder": "生日", 'type':'date',"class": "form-control"})
        )
    email = forms.EmailField(
        required=True,
        error_messages={
            "required": "信箱不能為空",
        },
        label='', 
        widget=forms.TextInput(attrs={"placeholder": "信箱", "class": "form-control"})
        )    
    address = forms.CharField(
        required=True,
        max_length=128,
        error_messages={
            "required": "地址不能為空",
        },
        label='', 
        widget=forms.TextInput(attrs={"placeholder": "地址", "class": "form-control"})
        )
    
    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'fullName', 'telephone','birthday','email', 'address']

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password!=password2:
            raise forms.ValidationError('密碼不相符')
        return password2

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(user.password)
        if commit:
            user.save()
        return user
class AskForm(forms.ModelForm):
    asktype=forms.fields.ChoiceField(
        choices=((1,'訂單'),(2,'出貨'),(3,'退貨/退款'),(4,'取消訂單'),(5,'其他')),
        required=True,
        label='問題類型',
        widget=forms.widgets.RadioSelect
        )
    asktittle=forms.CharField(
        required=True,
        error_messages={
            "require":"標題不能空白",
        },
        label='發問標題',
        widget=forms.TextInput(attrs={"class":"form-control"})
        )
    ordernumber=forms.CharField(
        required=True,
        error_messages={
            "require":"請輸入訂單編號",
        },
        label='訂單編號',
        widget=forms.TextInput(attrs={"class":"form-control"})
        )
    suggest=forms.CharField(
        required=True,
        error_messages={
            "require":"問題與建議內容不能空白",
        },
        label='問題與建議',
        widget=forms.TextInput(attrs={"class":"form-control"})
        )
    class Meta:
        model = User
        fields = ['asktype','asktittle','ordernumber','suggest',]
        widgets ={'asktype':forms.RadioSelect}