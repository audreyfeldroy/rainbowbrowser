from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rainbow_proj.views.home', name='home'),
    url(r'^rainbows/', include('rainbows.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
