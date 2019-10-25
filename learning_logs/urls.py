"""定义learning_logs的URL模式"""
from django.urls import path, include,re_path

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^topics/$',views.topics, name='topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,name='edit_entry'),
]

app_name = 'learning_logs'
