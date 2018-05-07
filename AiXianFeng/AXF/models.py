from django.db import models

# Create your models here.


class Main(models.Model):
    img = models.CharField(max_length=200) #图片
    name = models.CharField(max_length=100) # 名称
    trackid = models.CharField(max_length=16) # 通用id

    class Meta:
        abstract = True


class MainWheel(Main):
    # 轮播banner
    class Meta:
        db_table = 'main_wheel'


class MainNav(Main):
    # 导航
    class Meta:
        db_table = 'main_nav'


class MainMustBuy(Main):
    # 必购
    class Meta:
        db_table = 'main_mustbuy'


class MainShop(Main):
    # 商店
    class Meta:
        db_table = 'main_shop'


# 主要展示的商品
class MainShow(Main):

    categoryid = models.CharField(max_length=16)  # 商品类别
    categoryname = models.CharField(max_length=100)  # 品牌名称
    img1 = models.CharField(max_length=200)  # 图片
    childcid1 = models.CharField(max_length=16)  # 关联表id
    productid1 = models.CharField(max_length=16)  # 产品id
    longname1 = models.CharField(max_length=100)  # 产品名称
    discountprice1 = models.FloatField(default=0)  # 折扣价格
    price1 = models.FloatField(default=1)  # 商品价格
    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=16)
    productid2 = models.CharField(max_length=16)
    longname2 = models.CharField(max_length=100)
    discountprice2 = models.FloatField(default=0)
    price2 = models.FloatField(default=1)
    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=16)
    productid3 = models.CharField(max_length=16)
    longname3 = models.CharField(max_length=100)
    discountprice3 = models.FloatField(default=0)
    price3 = models.FloatField(default=1)


    class Meta:
        db_table = 'main_show'


class FoodType(models.Model):
    typeid = models.CharField(max_length=16)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField(default=1)

    class Meta:
        db_table = 'food_types'


class Goods(models.Model):
    ''' 商品数据库 '''
    productid = models.CharField(max_length=6)  # 商品 id
    productimg = models.CharField(max_length=200)  # 商品图片url
    productname = models.CharField(max_length=100)  # 商品名称
    productlongname = models.CharField(max_length=200)  # 商品规格
    isxf = models.IntegerField(default=1)
    pmdesc = models.CharField(max_length=100)
    specifics = models.CharField(max_length=100)  # 规格
    discountprice = models.FloatField(default=0)  # 折后价格
    price = models.FloatField(default=1)  # 原价
    categoryid = models.CharField(max_length=16)  # 分类id
    childcid = models.CharField(max_length=16)  # 子分类id
    childcidname = models.CharField(max_length=100, null=True)
    dealerid = models.CharField(max_length=16)
    storenums = models.IntegerField(default=1)  # 排序
    productnum = models.IntegerField(default=1)  # 销量排序

    class Meta:
        db_table = 'Goods'


class User(models.Model):
    username = models.CharField(max_length=32, unique=True)  # 名称
    password = models.CharField(max_length=256)  # 密码
    email = models.CharField(max_length=64, unique=True)  # 邮箱
    # false 代表nv
    sex = models.BooleanField(default=False)
    icon = models.ImageField(upload_to='icon')  # 头像
    is_delete = models.BooleanField(default=False)  # 删除

    class Meta:
        db_table = 'axf_user'


# 购物车

class Cart(models.Model):
    user = models.ForeignKey(User)  # 关联用户
    goods = models.ForeignKey(Goods)  # 关联商品
    c_num = models.IntegerField(default=1)  # 商品的个数
    is_select = models.BooleanField(default=True)  # 是否选择商品

    class Meta:
        db_table = 'axf_cart'


class Order(models.Model):
    user = models.ForeignKey(User)  # 关联用户
    o_num = models.CharField(max_length=64)
    # 0 代表已下单,但是未付款， 1 已付款未发货 2 已付款 已发货
    o_status = models.IntegerField(default=0)  # 状态
    o_create = models.DateTimeField(auto_now_add=True)  # 创建时间

    class Meta:
        db_table = 'axf_order'


class OrderGoods(models.Model):
    goods = models.ForeignKey(Goods)  # 关联商品
    order = models.ForeignKey(Order)  # 关联订单
    goods_num = models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_order_goods'
