# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic.base import RedirectView
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import UpdateView
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response, Http404, redirect
from django.contrib.auth import get_user
from django.contrib import messages
from braces.views import LoginRequiredMixin
from carton.cart import Cart
from mcat.models import Product
from mcat_order.models import Customer, Order, OrderedProduct
from mcat_order.forms import CustomerForm


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
def order_dispatcher(request):
    if request.is_ajax():
        if request.user.is_authenticated():
            # is there a customer for this user?
            return HttpResponse("<script>self.location.href='"+reverse('mcat-customer-form')+"'</script>")
        else:
            login_url = settings.LOGIN_URL+'?next='+reverse('mcat-customer-form')
            signup_url = reverse('account_signup')+'?next='+reverse('mcat-customer-form')
            return render_to_response('mcat_order/login_choice.html',
                                      {'login_url' : login_url, 'signup_url' : signup_url},
                                       context_instance=RequestContext(request),
                                       content_type="application/xhtml+xml"
                                       )
    else:
        if settings.DEBUG:
            print "Not ajax request"
        raise Http404


class CustomerFormView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'mcat_order/customer_form.html'
    
    def dispatch(self, request, *args, **kwargs):
        if Customer.objects.filter(user=request.user).exists():
            return redirect('mcat-confirm-order')
        return super(CustomerFormView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(CustomerFormView, self).get_context_data(**kwargs)
        context['no_cart_icon'] = True
        return context
    
    def get_login_url(self):
        return settings.LOGIN_URL+'?next='+reverse('mcat-customer-form')
    
    def get_success_url(self):
        return reverse('mcat-confirm-order')
    
    def form_valid(self, form, **kwargs):
        if self.request.method == "POST":
            obj = form.save(commit=False)
            obj.user = self.request.user
        else: 
            raise Http404
        return super(CustomerFormView, self).form_valid(form)


class ConfirmOrderView(LoginRequiredMixin, TemplateView):
    template_name = 'mcat_order/confirm_order.html'
    
    def get_login_url(self):
        return settings.LOGIN_URL+'?next='+reverse('mcat-confirm-order')
    
    def get_context_data(self, **kwargs):
        context = super(ConfirmOrderView, self).get_context_data(**kwargs)
        context['customer'] = get_object_or_404(Customer, user=self.request.user)
        context['no_cart_icon'] = True
        return context


class CustomerUpdateFormView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'mcat_order/customer_update_form.html'
    
    def get_success_url(self):
        return reverse('mcat-confirm-order')

   
class PostOrderView(LoginRequiredMixin, TemplateView):
    template_name = 'mcat_order/posted_order.html'
    login_url = settings.LOGIN_URL
    
    def dispatch(self, request, *args, **kwargs):
        self.customer = get_object_or_404(Customer, user=self.request.user)
        #~ create the order
        cart = Cart(request.session)
        if cart.count == 0:
            messages.warning(self.request, _(u'The cart is empty: order cancelled'))
            return super(PostOrderView, self).dispatch(request, *args, **kwargs)
        order = Order.objects.create(customer=self.customer, total=cart.total)
        for item in cart.items:
            #~ get the product
            OrderedProduct.objects.create(product=item.product, order=order, quantity=item.quantity, price_per_unit=item.product.price)
        
        cart.clear()
        return super(PostOrderView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(PostOrderView, self).get_context_data(**kwargs)
        context['customer'] = self.customer
        context['no_cart_icon'] = True
        return context
    


