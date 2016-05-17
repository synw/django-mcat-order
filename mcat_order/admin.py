# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from mcat_order.models import Customer, Order, OrderedProduct


class OrderdedProductInline(admin.TabularInline):
    model = OrderedProduct
    fields = ['product', 'order', 'quantity', 'price_per_unit']
    readonly_fields = ['order', 'quantity', 'price_per_unit']
    extra = 0


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'telephone', 'email', 'user']
    list_select_related = ['user']
    search_fields = ['last_name', 'user__username', 'email', 'telephone']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['created', 'customer', 'total', 'status']
    list_select_related = ['customer']
    search_fields = ['customer__last_name', 'customer__email', 'customer__telephone']
    list_filter = ['status']
    attrs = {'class': 'special', 'size': '40'}
    fields = ['created', 'customer', 'status', 'total']
    readonly_fields = ['created', 'total']
    inlines = [OrderdedProductInline]