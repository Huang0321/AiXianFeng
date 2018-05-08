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

