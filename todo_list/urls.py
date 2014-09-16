from django.conf.urls import patterns, url

from todo_list import views

urlpatterns = patterns('', url(r'^$', views.index, name='index'),)
