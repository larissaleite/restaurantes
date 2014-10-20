from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'clientes.views.index'),
    url(r'^cadastro/$', 'clientes.views.cadastro'),
    url(r'^pratos/$', 'clientes.views.pratos'),
    url(r'^login/$', 'clientes.views.login'),
    url(r'^carrinho/$', 'clientes.views.carrinho'),
    url(r'^pratos/carrinho$', 'clientes.views.adicionar_pratos_carrinho'),
)
