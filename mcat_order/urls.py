# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from mcat_order.views import add_to_cart, clear_cart, remove_from_cart, CustomerFormView, order_dispatcher, ConfirmOrderView, CustomerUpdateFormView

urlpatterns = patterns('', 
url(r'^cart/add/(?P<slug>[-_\w]+)/$', add_to_cart, name="add-to-cart"),
url(r'^cart/remove/(?P<slug>[-_\w]+)/$', remove_from_cart, name="remove-from-cart"),
url(r'^cart/clear/$', clear_cart, name="clear-cart"),
url(r'^now/$', order_dispatcher, name="mcat-order-login-dispatcher"),
url(r'^customer/$', CustomerFormView.as_view(), name="mcat-customer-form"),
url(r'^customer/update/(?P<pk>[0-9]+)/$', CustomerUpdateFormView.as_view(), name="mcat-update-customer-form"),
url(r'^confirm/$', ConfirmOrderView.as_view(), name="mcat-confirm-order"),
)

