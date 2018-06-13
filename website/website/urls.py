# coding: utf-8

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^sass/(?P<path>.+\.css)$', views.compile_sass, name='sass'),
    url(r'index/$', views.index),
] + static(settings.STATIC_URL)
