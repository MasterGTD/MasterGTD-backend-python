# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import json
# Create your views here.

def index(request):
    return HttpResponse("Welcome to MasterGTD")
