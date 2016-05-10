# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from mcat_order.views import add_to_cart, clear_cart, remove_from_cart

urlpatterns = patterns('', 
url(r'^cart/add/(?P<slug>[-_\w]+)/$', add_to_cart, name="add-to-cart"),
url(r'^cart/remove/(?P<slug>[-_\w]+)/$', remove_from_cart, name="remove-from-cart"),
url(r'^cart/clear/$', clear_cart, name="clear-cart"),
)

