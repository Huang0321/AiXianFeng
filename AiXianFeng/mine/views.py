
from django.shortcuts import render

from AXF.models import Order


def mine_home(request):

    if request.method == 'GET':
        users1 = request.user.order_set.filter(o_status=0)  # 获取已下单未付款的对象set
        users2 = request.user.order_set.filter(o_status=1)  # 获取已付款未收货的对象set
        num1 = 0
        num2 = 0
        if users1:
            for user in users1:
                num1 += user.o_num  # 已下单未付款的订单总数
        if users2:
            for user in users2:
                num2 += user.o_num   # 已付款未收货的订单总数

        return render(request, 'mine/mine.html', {'num1': num1, 'num2': num2})


def not_pay(request):
    # 通过用户找到订单对象set
    orders_not_pay = request.user.order_set.filter(o_status=0)

    goods_not_pay = []  # 先设一个未付款的商品对象set

    # 判断是否存在未付款的订单 或 未收货的订单
    if orders_not_pay:
        # 通过未完成的订单找到对应的 商品订单 信息 set
        goods_order_not_pay = orders_not_pay[0].ordergoods_set
        if goods_order_not_pay:
            # 通过 商品订单 信息找到对应的 商品set
            for good in goods_order_not_pay:
                goods_not_pay += good.goods  # 将订单对象set相加
        else:
            goods_not_pay = []
    else:
        goods_not_pay = []

    # 与上面相同


    return render(request, 'order/order_list_wait_pay.html', {'goods_not_pay': goods_not_pay})


def not_recieve(request):

    orders_not_recieve = request.user.order_set.filter(o_status=1)
    goods_not_recieve = []  # 先设一个未收货的商品对象set
    if orders_not_recieve:
        goods_order_not_recieve = orders_not_recieve[0].ordergoods_set
        if goods_order_not_recieve:
            for good in goods_order_not_recieve:
                goods_not_recieve += good.goods
        else:
            goods_not_recieve = []
    else:
        goods_not_recieve = []

    return render(request, 'order/order_list_payed.html', {'goods_not_recieve': goods_not_recieve})