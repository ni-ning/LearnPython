from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == "POST":
        username = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user = auth.authenticate(username=username, password=pwd)

        # if验证成功返回user对象，否则返回None
        if user:
            auth.login(request, user)       # request.user 当前登录对象
            next_url = request.GET.get('next', '/index/')
            return redirect(next_url)
        else:
            # request.user 为匿名用户对象
            return HttpResponse('用户名或密码错误')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/login')


def index(request):
    print(request.session.get('_auth_user_hash'))
    print(request.session.get('_auth_user_backend'))

    return render(request, 'index.html')


def reg(request):
    if request.method == "POST":
        username = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user = User.objects.create_user(username=username, password=pwd)
        if user:
            return HttpResponse('注册成功')

    return render(request, 'reg.html')


@login_required
def order(request):
    return HttpResponse('登录后Order')

