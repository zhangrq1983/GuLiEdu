from django.shortcuts import render, redirect, reverse, HttpResponse
from .forms import *
from .models import UserProfile, EmailVerifyCode, BannerInfo
# from tools.send_mail_tool import send_email_code
from django.db.models import Q
from django.contrib.auth import authenticate,logout,login

def index(request):
    return render(request, 'index.html')


def user_register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            email = user_register_form.cleaned_data['email']
            password = user_register_form.cleaned_data['password']

            user_list = UserProfile.objects.filter(Q(username=email) | Q(email=email))
            if user_list:
                # return render(request, 'users/register.html', {
                return render(request, 'register.html', {
                    'msg': '用户已经存在'
                })
            else:
                a = UserProfile()
                a.username = email
                a.set_password(password)
                a.email = email
                a.save()
                # send_email_code(email, 1)
                # return HttpResponse('请尽快前往您的邮箱激活，否则无法登陆')
                return redirect(reverse('index'))
        else:
            # return render(request, 'users/register.html', {
            return render(request, 'register.html', {
                'user_register_form': user_register_form
            })


def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            username = user_login_form.cleaned_data['username']
            password = user_login_form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('index'))
            else:
                return render(request, 'login.html', {
                    'msg': '邮箱或密码有误'
                })
        else:
            return render(request, 'login.html', {
                'user_login_form': user_login_form
            })