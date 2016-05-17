# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import formats
from django.contrib.auth.models import User
from jsonfield import JSONField
from mbase.models import MetaBaseModel, MetaBaseStatusModel
from mcat.models import Product
from mcat_order.conf import ORDER_STATUSES, CIVILITIES


class Customer(MetaBaseModel, MetaBaseStatusModel):
    first_name = models.CharField(max_length=120, verbose_name=_(u'First name'))
    last_name = models.CharField(max_length=120, verbose_name=_(u'Last name'))
    civility = models.CharField(max_length=60, verbose_name=_(u'Title'), choices=CIVILITIES, default=CIVILITIES[0][0])
    telephone = models.PositiveIntegerField(verbose_name=_(u'Phone number'))
    company_name = models.CharField(max_length=120, blank=True, verbose_name=_(u'Company name'))
    email = models.EmailField(verbose_name=_(u'Email'))
    address = models.TextField(verbose_name=_(u'Address'))
    user = models.OneToOneField(User, verbose_name=_(u'User') )
    extra = JSONField(blank=True, verbose_name=_(u'Extra infos'))
    
    class Meta:
        verbose_name=_(u'Customer')
        verbose_name_plural = _(u'Customers')
        ordering = ('last_name',)
        unique_together = ('first_name', 'last_name')

    def __unicode__(self):
        return unicode(self.first_name+' '+self.last_name)

    @property
    def telephone_formated(self):
        return '%s %s %s %s' %(self.telephone[0:2],self.telephone[2:4],self.telephone[4:6],self.telephone[6:8])
    
    def get_civility(self):
        for civ in CIVILITIES:
            if civ[0] == self.civility:
                return civ[1]
        return self.civility
 
   
class Order(MetaBaseModel):
    customer = models.ForeignKey(Customer, related_name='orders', verbose_name=_(u'Customer'))
    status = models.CharField(max_length=120, verbose_name=_(u'Status'), choices=ORDER_STATUSES, default=ORDER_STATUSES[0][0])
    total = models.FloatField(null=True, blank=True, verbose_name=_(u'Total'))

    class Meta:
        verbose_name=_(u'Order')
        verbose_name_plural = _(u'Orders')
        ordering = ('-created',)

    def __unicode__(self):
        date = formats.date_format(self.created, "SHORT_DATETIME_FORMAT")
        return unicode(date+' - '+str(self.total)+' - '+self.status)

    
class OrderedProduct(MetaBaseModel):
    product = models.ForeignKey(Product, related_name='ordered', verbose_name=_(u'Product'))
    order = models.ForeignKey(Order, related_name='+', verbose_name=_(u'Order'))
    quantity = models.PositiveIntegerField(verbose_name=_(u'Quantity'))
    price_per_unit = models.FloatField(verbose_name=_(u'Price per unit'))
    
    class Meta:
        verbose_name=_(u'Ordered product')
        verbose_name_plural = _(u'Ordered products')
        ordering = ('-created', 'order')

    def __unicode__(self):
        date = formats.date_format(self.created, "SHORT_DATETIME_FORMAT")
        return unicode(date)
    


