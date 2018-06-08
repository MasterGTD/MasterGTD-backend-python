# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import *
# Create your views here.


def index(request):
    return HttpResponse("Welcome to MasterGTD")


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            username=username,
            password=password
        )
        if user is not None:
            if user.is_active:
                login(request, user)
                return JsonResponse({
                    'result': 'success',
                    'data': 'username',
                    'value': 'login success'
                    # token?
                })
            else:
                return JsonResponse({
                    'result': 'fail',
                    'data': '',
                    'value': 'user is not active'
                })
        else:
            return JsonResponse({
                    'result': 'fail',
                    'data': '',
                    'value': 'no such user'
                })
    return JsonResponse({
                'result': 'fail',
                'data': '',
                'value': 'method error'
            })


@csrf_exempt
def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        new_user = User.objects.create_user(username, email, password)
        new_user.save()
        # new_user = authenticate(
        #     username=form.cleaned_data['username'],
        #     password=form.cleaned_data['password1'],
        # )
        login(request, new_user)
        return JsonResponse({
                    'result': 'success',
                    'data': 'username',
                    'value': 'register success'
                    # token?
                })
    return JsonResponse({
                'result': 'fail',
                'data': '',
                'value': 'method error'
            })


@csrf_exempt
def user_logout(request):
    logout(request)
    return JsonResponse({
        'result': 'success',
        'data': 'username',
        'value': 'logout success'
    })


@csrf_exempt
def get_tag(request):
    if request.method == "POST" :
        tag_name = request.POST.get("name")
        tag = Tag.objects.get_or_create(text=tag_name)[0]
        return JsonResponse({
            'result': 'success',
            'data': {
                'name': tag_name,
                'slug': tag.slug
            },
            'value': 'Create tag success.'
        })
    return JsonResponse({
            'result': 'fail',
            'data': '',
            'value': 'method error'
        })


@csrf_exempt
def get_category(request):
    if request.method == "POST":
        cate_name = request.POST.get("name")
        cate = Category.objects.get_or_create(name=cate_name)[0]
        return JsonResponse({
            'result': 'success',
            'data': {
                'name': cate.name,
                'slug': cate.slug,
                'proCount': cate.pro_count
            },
            'value': 'Create category success.'
        })
    return JsonResponse({
        'result': 'fail',
        'data': '',
        'value': 'method error'
    })


def test_magic(request):
    return render(request, 'test_magic.html')