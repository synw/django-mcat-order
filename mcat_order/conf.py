# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


ORDER_STATUSES = (
                  ('pending', _(u'Pending')),
                  ('success', _(u'Success')),
                  ('failed', _(u'Failed')),
                  )

CIVILITIES = (
              ('mr', 'Mr'),
              ('mm', 'Mme'),
              )

ORDER_STATUSES = getattr(settings, 'MCAT_ORDER_STATUSES', ORDER_STATUSES)

CIVILITIES = getattr(settings, 'MCAT_CIVILITIES', CIVILITIES)

