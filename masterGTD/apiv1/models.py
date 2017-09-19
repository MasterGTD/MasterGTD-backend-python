# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone

from pypinyin import lazy_pinyin as lp
# Create your models here.


class Tag(models.Model):
    text = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.text

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = '-'.join(lp(str(self.text))) + str(self.pk)
        super(Tag, self).save(force_insert=False, force_update=False, using=None, update_fields=None)


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    pro_count = models.IntegerField()

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = '-'.join(str(self.name))
        super(Category, self).save(force_insert=False, force_update=False, using=None, update_fields=None)


class Project(models.Model):
    name = models.CharField(max_length=200, unique=False)
    slug = models.CharField(max_length=200, unique=False)
    desc = models.TextField()
    is_public = models.BooleanField()
    category = models.ForeignKey(Category, models.SET_NULL, null=True,
                                 related_name="projects",
                                 related_query_name="category")
    user = models.ForeignKey(User, related_name="projects", related_query_name="user")

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = '-'.join(lp(str(self.name))) + str(self.pk)
        super(Project, self).save(force_insert=False, force_update=False, using=None, update_fields=None)


class CheckList(models.Model):
    name = models.CharField(max_length=200, unique=False)
    of_project = models.ForeignKey(Project, related_name="lists", related_query_name="project")

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=300, unique=False)
    is_finished = models.BooleanField()
    of_list = models.ForeignKey(CheckList, related_name="tasks", related_query_name='list')

    def __str__(self):
        return self.name
