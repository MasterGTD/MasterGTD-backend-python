from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^userlogin/$', user_login),
    url(r'^userregister/$', user_register),
    url(r'^userlogout/$', user_logout),
    url(r'^gettag/$', get_tag),
    url(r'^getcategory/$', get_category),
    url(r'^testmagic/$', test_magic),
]