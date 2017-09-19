from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^userLogin/$', user_login),
    url(r'^userRegister/$', user_register),
    url(r'^userLogout/$', user_logout)
]