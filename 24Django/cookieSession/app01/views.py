from django.shortcuts import render, HttpResponse


def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        if user == 'linda' and pwd == '456':
            response = HttpResponse('登录成功')
            response.set_cookie('is_login', True)

            import datetime
            date = datetime.datetime(2019, 5, 1)
            # response.set_cookie('username', user, expires=date)
            response.set_cookie('username', user, path='/index')
            # response.delete_cookie('username')

            return response

    return render(request, 'login.html')


def index(request):
    print(request.COOKIES)
    is_login = request.COOKIES.get('is_login')
    username = ''
    if is_login:
        username = request.COOKIES.get('username')

    return render(request, 'index.html', {'username': username})


def test(request):
    print(request.COOKIES)
    return HttpResponse('TEST')


def login_session(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'tom' and pwd == '111':
            print(user, ' and ', pwd)
            request.session['login'] = True
            request.session['user'] = 'tom'
            """
            1. 生成随机字符串 '345djigjdjijagid'
            2. response.set_cookie('sessionid', '345djigjdjijagid')
            3. 在django_session表中创建一条记录：
                session_key         session_data
                345djigjdjijagid    {"is_login": True, "username": "linda"}
            """
            return HttpResponse('登录成功')

    return render(request, 'login.html')


def index_session(request):
    if request.session.get('login'):
        """
        1. request.COOKIES.get('sessionid')  得到随机字符串 '345djigjdjijagid'
        2. django_session 表中过滤记录 '345djigjdjijagid'
        3. 取得 session_data
        """
        print(dict(request.session))
        return HttpResponse('session_index page')

