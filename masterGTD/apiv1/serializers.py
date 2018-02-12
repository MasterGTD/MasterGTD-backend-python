from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class HabitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'


class HabitDaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HabitDay
        fields = '__all__'


class PercentTodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PercentTodo
        fields = '__all__'


class CheckListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CheckList
        fields = '__all__'


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
