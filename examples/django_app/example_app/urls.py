from django.conf.urls import include, url
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from chatterbot.ext.django_chatterbot import urls as chatterbot_urls
from example_app.views import ChatterBotAppView
from . import views
from saved_posts import urls as saved_posts_urls

urlpatterns = [
    url(r'^$', ChatterBotAppView.as_view(), name='main'),
    url(r'^register/', views.UserFormView.as_view(), name='register'),
    #url(r'^login/', views.UserLoginView.as_view(), name='login'),
    url(r'^login/$', auth.views.login, {"template_name": "login.html"}, name='login'),
    url(r'^logout/', auth.views.logout, {'next_page': '/'}, name='logout'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^api/chatterbot/', include(chatterbot_urls, namespace='chatterbot')),
    url(r'^notebook/', include(saved_posts_urls), name="notebook"),
    url(r'^about/$', views.AboutView.as_view(), name="about"),
]
