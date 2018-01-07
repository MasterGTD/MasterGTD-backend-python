from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Todo)
admin.site.register(Habit)
admin.site.register(HabitDay)
admin.site.register(PercentTodo)
admin.site.register(Project)
admin.site.register(CheckList)
admin.site.register(Task)