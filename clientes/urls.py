from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'clientes.views.index'),
    url(r'^cadastro/$', 'clientes.views.cadastro'),
    url(r'^pratos/$', 'clientes.views.pratos'),
)
