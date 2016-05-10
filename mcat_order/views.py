# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response, Http404, redirect
from django.contrib.auth import get_user
from carton.cart import Cart
from mcat.models import Product
from mcat_order.models import Customer
from mcat_order.forms import LoginForm, CustomerForm


# =================================== Cart views ===========================
def add_to_cart(request, slug):
    if request.is_ajax():
        cart = Cart(request.session)
        product = get_object_or_404(Product, slug=slug)
        cart.add(product, price=product.price)
        return render_to_response('mcat_order/cart.html',
                                   {'product' : product},
                                   context_instance=RequestContext(request),
                                   content_type="application/xhtml+xml"
                                   )
    else:
        if settings.DEBUG:
            print "Not ajax request"
        raise Http404
    
def remove_from_cart(request, slug):
    if request.is_ajax():
        cart = Cart(request.session)
        product = get_object_or_404(Product, slug=slug)
        cart.remove_single(product)
        return render_to_response('mcat_order/cart.html',
                                   context_instance=RequestContext(request),
                                   content_type="application/xhtml+xml"
                                   )
    else:
        if settings.DEBUG:
            print "Not ajax request"
        raise Http404

def clear_cart(request):
    if request.is_ajax():
        cart = Cart(request.session)
        cart.clear()
        return render_to_response('mcat_order/cart.html',
                                   context_instance=RequestContext(request),
                                   content_type="application/xhtml+xml"
                                   )
    else:
        if settings.DEBUG:
            print "Not ajax request"
        raise Http404

# =================================== Order views ===========================
def order_login_form(request):
    form = LoginForm()
    if request.is_ajax():
        # check if a customer exists
        customer = None
        if request.user.is_authenticated():
            try:
                customer = Customer.objects.get(user=get_user(request))
            except ObjectDoesNotExist:
                pass
        return render_to_response('mcat_order/order_form.html',
                                  {'customer' : customer, 'form': form},
                                   context_instance=RequestContext(request),
                                   content_type="application/xhtml+xml"
                                   )
    else:
        if settings.DEBUG:
            print "Not ajax request"
        raise Http404


def customer_form(request):
    form = CustomerForm()
    if request.is_ajax():
        # check if a customer exists
        customer = None
        if request.user.is_authenticated():
            try:
                customer = Customer.objects.get(user=get_user(request))
            except ObjectDoesNotExist:
                pass
        return render_to_response('mcat_order/customer_form.html',
                                  {'customer' : customer, 'form': form},
                                   context_instance=RequestContext(request),
                                   content_type="application/xhtml+xml"
                                   )
    else:
        if settings.DEBUG:
            print "Not ajax request"
        raise Http404




