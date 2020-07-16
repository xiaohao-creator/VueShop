# -*- coding: utf-8 -*-
# @Author  : xiaohao
# @Email   : 321459055@qq.com
# @File    : filters.py
# @Software: PyCharm
# @Time    : 2020/7/15 22:05

from rest_framework import generics
from django_filters import rest_framework as filters

from goods.models import Goods


class GoodsFilter(filters.FilterSet):
    """
    商品的过滤类
    """
    price_min = filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    price_max = filters.NumberFilter(field_name="shop_price", lookup_expr='lte')

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max']
