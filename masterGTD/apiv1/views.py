# -*- coding: utf-8 -*-

from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from .models import *
from .serializers import *
# Create your views here.


def index(request):
    return HttpResponse("Welcome to MasterGTD")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('-date_joined')
    serializer_class = GroupSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tag.objects.all().order_by('-id')
    serializer_class = TagSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-id')
    serializer_class = TodoSerializer


class HabitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Habit.objects.all().order_by('-id')
    serializer_class = HabitSerializer


class HabitDayViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = HabitDay.objects.all().order_by('-id')
    serializer_class = HabitDaySerializer


class PercentTodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PercentTodo.objects.all().order_by('-id')
    serializer_class = PercentTodoSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all().order_by('-id')
    serializer_class = ProjectSerializer


class CheckListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CheckList.objects.all().order_by('-id')
    serializer_class = CheckListSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer

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
