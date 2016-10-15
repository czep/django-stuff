from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.stuff_list, name='stuff_list'),
  url(r'^new', views.stuff_create, name='stuff_new'),
  url(r'^edit/(?P<pk>\d+)$', views.stuff_update, name='stuff_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.stuff_delete, name='stuff_delete'),
]
