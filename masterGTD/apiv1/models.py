# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from pypinyin import lazy_pinyin as lp
# Create your models here.

# 标签（Tag）
class Tag(models.Model):
    tag_text = models.CharField(max_length=200, unique=True)
    tag_slug = models.CharField(max_length=200)

    def __unicode__(self):
        return self.tag_text

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.tag_slug = '-'.join(lp(str(self.tag_text)))
        super(Tag, self).save(force_insert=False, force_update=False, using=None,
                              update_fields=None)

class Project(models.Model):
    pro_name = models.CharField(max_length=200, unique=False)
    pro_slug = models.CharField(max_length=200)

    def __unicode__(self):
        return self.pro_name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.pro_slug = '-'.join(lp(str(self.pro_name)))
        super(Project, self).save(force_insert=False, force_update=False, using=None,
             update_fields=None)