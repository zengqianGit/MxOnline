# _*_ coding: utf-8 _*_
__author__ = 'qianzeng'
__date__ = '2018/3/6 17:51'
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)
