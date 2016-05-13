# -*- coding: utf-8 -*-

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class McatOrderConfig(AppConfig):
    name = "mcat_order"
    verbose_name = _(u"Catalog orders")
    
    def ready(self):
        pass

