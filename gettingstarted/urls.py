from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import automation.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', automation.views.index, name='index'),
    url(r'^db', automation.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', automation.views.login, name='login'),
    url(r'^logout', automation.views.logout, name='logout'),
)
