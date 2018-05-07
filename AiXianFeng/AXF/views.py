from django.shortcuts import render
from time import time
import random

# Create your views here.
from AXF.models import MainWheel, MainNav, MainMustBuy, MainShop, MainShow, User


def home(request):

    if request.method == 'GET':
        wheel_data = MainWheel.objects.all()
        nav_data = MainNav.objects.all()
        must_buy_data = MainMustBuy.objects.all()
        shop_data = MainShop.objects.all()
        show_data = MainShow.objects.all()

        return render(request, 'home/home.html', {'wheel_data': wheel_data, 'nav_data': nav_data,
                                                  'must_buy_data': must_buy_data, 'shop_data': shop_data,
                                                  'show_data': show_data})


def login(request):

    if request.method == 'GET':

        return render(request, 'user/user_login.html')

    if request.method == 'POST':
        #获取用户登录名和密码
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        try:
            user = User.objects.get(username)
            if user:   # 验证用户是否存在
                if pwd == user.password:
                    letters = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    ticket = ''
                    for _ in range(15):
                        ticket += random.choice(letters)
                    ticket += str(time())
                    user.update(ticket)
                    return render(request, 'home/home.html')

                else:
                    pwd_erro_data = '密码错误'
                    return render(request, 'user/user_login.html', {'pwd_erro_data': pwd_erro_data})

        except Exception as e:
            user_erro_data = '用户名错误'
            return render(request, 'user/user_login.html', {'usre_erro_data': user_erro_data})

