# -*- coding: utf-8 -*-

from django import forms
from mcat_order.models import Customer
from django.contrib.auth.models import User

     
class CustomerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['civility'].label = ''
        return
    
    class Meta:
        model = Customer
        fields = ['civility', 'first_name', 'last_name', 'telephone', 'email', 'address']
        widgets = {'civility': forms.RadioSelect()}
