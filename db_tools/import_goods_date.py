# -*- coding: utf-8 -*-
# @Author  : xiaohao
# @Email   : 321459055@qq.com
# @File    : import_goods_date.py
# @Software: PyCharm
# @Time    : 2020/7/14 17:55

import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VueShop.settings')

import django
django.setup()

from goods.models import Goods
from goods.models import GoodsCategory
from goods.models import GoodsImage

from db_tools.data.product_data import row_data

for goods_detail in row_data:
    goods = Goods()
    goods.name = goods_detail["name"]
    goods.market_price = float(int(goods_detail["market_price"].replace("￥", "").replace("元", "")))
    goods.shop_price = float(int(goods_detail["sale_price"].replace("￥", "").replace("元", "")))
    goods.goods_brief = goods_detail["desc"] if goods_detail['desc'] is not None else ""
    goods.goods_desc = goods_detail["goods_desc"] if goods_detail['goods_desc'] is not None else ""
    goods.goods_front_image = goods_detail["images"][0] if goods_detail["images"] else ""

    category_name = goods_detail["categorys"][-1]
    category = GoodsCategory.objects.filter(name=category_name)
    if category:
        goods.category = category[0]
    goods.save()

    goods_image_instance = GoodsImage()
    goods_image_instance.goods = goods
    for goods_image in goods_detail['images']:
        goods_image_instance.image = goods_image
        goods_image_instance.save()
