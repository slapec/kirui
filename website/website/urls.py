from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'static/kirui/css/kirui.css', views.kirui_css),
    url(r'index/$', views.index),
] + static(settings.STATIC_URL)
