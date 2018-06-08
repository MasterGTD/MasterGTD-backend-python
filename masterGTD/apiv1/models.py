# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone

from pypinyin import lazy_pinyin as lp
# Create your models here.


class Tag(models.Model):
    '''标签组织'''
    text = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True, null=True)

    def __str__(self):
        return self.text

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Tag, self).save(force_insert=False, force_update=False, using=None, update_fields=None)
        self.slug = '-'.join(lp(str(self.text))) + str(self.pk) # 之后对pk加个加密啥的
        super(Tag, self).save(force_insert=False, force_update=False, using=None, update_fields=None)


class Category(models.Model):
    """任务所归的目录（工作，学习之类的）"""
    name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    pro_count = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = '-'.join(lp(str(self.name)))
        super(Category, self).save(force_insert=False, force_update=False, using=None, update_fields=None)


class Todo(models.Model):
    """各类型任务的基类"""
    name = models.CharField(max_length=200, unique=False)
    slug = models.CharField(max_length=200, unique=True)
    desc = models.TextField()
    is_public = models.BooleanField(default=True, null=False, blank=True) # 是否公开
    category = models.ForeignKey(Category, null=True,
                                 related_name="Todos",
                                 related_query_name="category",
                                 on_delete=models.SET_NULL)
    user = models.ForeignKey(User, related_name="Todos", related_query_name="user", on_delete=models.CASCADE)
    start_day = models.DateField(auto_now_add=True) # 开始时间
    finish_day = models.DateField(null=True) # 结束时间
    tags = models.ManyToManyField(Tag, related_name="todos")

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = '-'.join(lp(str(self.name))) + str(self.pk)
        super(Todo, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

class Habit(Todo):
    """一个习惯型任务的一些属性"""
    done_today = models.BooleanField(default=False) # 今天是否完成
    finished_days = models.IntegerField() # 累计完成天数
    current_strike_days = models.IntegerField() # 当前连续天数
    longest_strike_days = models.IntegerField() # 最长连续天数


class HabitDay(models.Model):
    """记录习惯型任务的每天完成情况"""
    date = models.DateField(auto_now_add=True)
    done = models.BooleanField(default=False)
    done_time = models.DateTimeField(auto_now_add=True)
    habit = models.ForeignKey(Habit, related_name="days", related_query_name="habit", null=False, on_delete=models.CASCADE)
    def __str__(self):
        return (str)(self.date)
        

class PercentTodo(Todo):
    """百分比任务类型的属性"""
    percent = models.IntegerField(default=0) # 百分比
    total_count = models.IntegerField() # 总数
    current_count = models.IntegerField() # 当前进度


class Project(Todo):
    """项目型任务的属性"""
    expect_finish_date = models.DateField(null=True)
        
        
class CheckList(models.Model):
    name = models.CharField(max_length=200, unique=False)
    of_Project = models.ForeignKey(Project, null=True, related_name="lists", related_query_name="Todo", on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Task(models.Model):
    is_finished = models.BooleanField(default=False)
    of_list = models.ForeignKey(CheckList, null=True, related_name="tasks", related_query_name='list', on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
