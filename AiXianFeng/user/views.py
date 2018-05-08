import random

import time

from django.core.urlresolvers import reverse
from rest_framework import mixins, viewsets
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
from user.filters import UserFilters
from user.serializers import UserSerializers
from AXF.models import User
from user.models import Cookies


def regist(request):

    if request.method == 'GET':
        return render(request, 'user/user_register.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = make_password(request.POST.get('password'))
        icon = request.FILES.get('icon')

        User.objects.create(
            username=username,
            email=email,
            password=password,
            icon=icon,
        )
        return render(request, 'user/user_login.html')


def login(request):

    if request.method == 'GET':
        return render(request, 'user/user_login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        user = User.objects.filter(username=username)
        if user:
            password = request.POST.get('password')
            if check_password(password, user[0].password):
                u_id = user[0].id
                letters = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                create_time = int(time.time())
                ticket = ''
                for _ in range(15):
                    ticket += random.choice(letters)
                ticket += str(create_time)
                Cookies.objects.create(
                    ticket=ticket,
                    create_time=create_time,
                    u_id=u_id
                )
                response = HttpResponseRedirect(reverse('mine:mh'))
                response.set_cookie('ticket', ticket, max_age=3600)
                return response
            else:
                return HttpResponse('密码错误')
        else:
            return HttpResponse('用户名错误')


def logout(request):

    if request.method == 'GET':

        ticket = request.COOKIES.get('ticket')
        if ticket:
            # 删除表里的信息
            users = Cookies.objects.filter(ticket=ticket)
            users[0].delete()
        # 删除浏览器里的cookie
        response = HttpResponseRedirect(reverse('axf:home'))
        response.delete_cookie('ticket')
        return response


class LoginSerializers(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):

    queryset = User.objects.all()

    serializer_class = UserSerializers

    filter_class = UserFilters


