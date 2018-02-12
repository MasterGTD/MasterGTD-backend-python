from django.conf.urls import url, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'tags', TagViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'todos', TodoViewSet)
router.register(r'habits', HabitViewSet)
router.register(r'habit_days', HabitDayViewSet)
router.register(r'percent_todos', PercentTodoViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'checklists', CheckListViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    url(r'^$', index),
    url(r'^', include(router.urls)),
    # url(r'^userlogin/$', user_login),
    # url(r'^userregister/$', user_register),
    # url(r'^userlogout/$', user_logout),
    # url(r'^gettag/$', get_tag),
    # url(r'^getcategory/$', get_category),
]