from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from account.forms import UserForm
from account.forms import AskForm
from account.models import Ask

def register(request):
    '''
    Register a new user
    '''
    template = 'account/register.html'
    if request.method == 'GET':
        return render(request, template, {'userForm':UserForm()})

    # POST
    userForm = UserForm(request.POST)
    if not userForm.is_valid():
        return render(request, template, {'userForm':userForm})

    userForm.save()
    messages.success(request, '歡迎註冊')
    return redirect('main:main')

def login(request):
    '''
    Login an existing user
    '''
    template = 'account/login.html'
    if request.method == 'GET':
        return render(request, template)

    # POST
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not username or not password:    # Server-side validation
        messages.error(request, '請填資料')
        return render(request, template)

    user = authenticate(username=username, password=password)
    if not user:    # authentication fails
        messages.error(request, '登入失敗')
        return render(request, template)

    # login success
    auth_login(request, user)
    messages.success(request, '登入成功')
    return redirect('main:main')

def logout(request):
    '''
    Logout the user
    '''
    auth_logout(request)
    messages.success(request, '歡迎再度光臨')
    return redirect('main:main')

def account(request):
    '''
    Render the edit page
    '''
    return render(request, 'account/account.html')
def ask(request):
    '''
    Render the ask page
    '''
    asks = Ask.objects.all()
    print(asks)
    context = {'asks':asks}
    return render(request, 'account/ask.html',context)

def askCreate(request):
    '''
    Create a new answer
    '''
    template = 'account/askCreate.html'
    if request.method =='GET':
        return render(request, template, {'askForm':AskForm()})
    
    # POST
    askForm = AskForm(request.POST)
    if not askForm.is_valid():
        return render(request, template, {'askForm':askForm})
    askForm.save()
    messages.success(request, '問答紀錄已新增')
    return redirect( 'account:ask')