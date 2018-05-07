# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-07 07:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_num', models.IntegerField(default=1)),
                ('is_select', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'axf_cart',
            },
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=16)),
                ('typename', models.CharField(max_length=100)),
                ('childtypenames', models.CharField(max_length=200)),
                ('typesort', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'food_types',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=6)),
                ('productimg', models.CharField(max_length=200)),
                ('productname', models.CharField(max_length=100)),
                ('productlongname', models.CharField(max_length=200)),
                ('isxf', models.IntegerField(default=1)),
                ('pmdesc', models.CharField(max_length=100)),
                ('specifics', models.CharField(max_length=100)),
                ('discountprice', models.FloatField(default=0)),
                ('price', models.FloatField(default=1)),
                ('categoryid', models.CharField(max_length=16)),
                ('childcid', models.CharField(max_length=16)),
                ('dealerid', models.CharField(max_length=16)),
                ('storenums', models.IntegerField(default=1)),
                ('productnum', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'Goods',
            },
        ),
        migrations.CreateModel(
            name='MainMustBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'main_mustbuy',
            },
        ),
        migrations.CreateModel(
            name='MainNav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'main_nav',
            },
        ),
        migrations.CreateModel(
            name='MainShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'main_shop',
            },
        ),
        migrations.CreateModel(
            name='MainShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=16)),
                ('categoryid', models.CharField(max_length=16)),
                ('categoryname', models.CharField(max_length=100)),
                ('img1', models.CharField(max_length=200)),
                ('childcid1', models.CharField(max_length=16)),
                ('productid1', models.CharField(max_length=16)),
                ('longname1', models.CharField(max_length=100)),
                ('discountprice1', models.FloatField(default=0)),
                ('price1', models.FloatField(default=1)),
                ('img2', models.CharField(max_length=200)),
                ('childcid2', models.CharField(max_length=16)),
                ('productid2', models.CharField(max_length=16)),
                ('longname2', models.CharField(max_length=100)),
                ('discountprice2', models.FloatField(default=0)),
                ('price2', models.FloatField(default=1)),
                ('img3', models.CharField(max_length=200)),
                ('childcid3', models.CharField(max_length=16)),
                ('productid3', models.CharField(max_length=16)),
                ('longname3', models.CharField(max_length=100)),
                ('discountprice3', models.FloatField(default=0)),
                ('price3', models.FloatField(default=1)),
            ],
            options={
                'db_table': 'main_show',
            },
        ),
        migrations.CreateModel(
            name='MainWheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'main_wheel',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_num', models.CharField(max_length=64)),
                ('o_status', models.IntegerField(default=0)),
                ('o_create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'axf_order',
            },
        ),
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_num', models.IntegerField(default=1)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AXF.Goods')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AXF.Order')),
            ],
            options={
                'db_table': 'axf_order_goods',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=64, unique=True)),
                ('sex', models.BooleanField(default=False)),
                ('icon', models.ImageField(upload_to='icon')),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'axf_user',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AXF.User'),
        ),
        migrations.AddField(
            model_name='cart',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AXF.Goods'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AXF.User'),
        ),
    ]
