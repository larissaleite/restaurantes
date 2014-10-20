from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('restaurantes.core.urls')), #to support all urls defined in core.urls
    url(r'^admin/', include(admin.site.urls)),
)
