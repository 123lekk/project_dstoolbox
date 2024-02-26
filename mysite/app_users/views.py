from django.contrib.auth.decorators import login_required
from django.contrib import messages
from audioop import reverse
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from app_users.forms import  RegisterForm

# Create your views here.
def Register(req):
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f'คุณ {username} สมัครสามชิกสำเร็จ')
            return redirect('login')  
    else:
        form = RegisterForm()
    return render(req, 'users/register.html',{'form': form})
#password non12345678

def Login(req):
    return render(req, 'registration/login.html')


@login_required
def dashboard(req):
    return render(req, 'users/dashboard.html')