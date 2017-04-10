from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^create/$', views.SavedText_Create, name="create"),
    url(r'^$', views.SavedText_List, name="list"),
    url(r'^(?P<id>\d+)/delete/$', views.SavedText_Delete, name="delete"),
]
