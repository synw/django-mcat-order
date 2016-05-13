# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from mcat_order.models import Customer, Order


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'telephone', 'email', 'user']
    list_select_related = ['user']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass