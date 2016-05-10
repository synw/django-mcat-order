# -*- coding: utf-8 -*-

from django import forms
from mcat_order.models import Customer
from django.contrib.auth.models import User

     
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'civility', 'telephone', 'email', 'address']
        widgets = {'civility': forms.RadioSelect}
        

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']