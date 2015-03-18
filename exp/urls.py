from django.conf.urls import patterns, include, url
from django.contrib import admin
from seguimiento.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'exp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', index),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
)
