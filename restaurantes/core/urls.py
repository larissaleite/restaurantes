from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'restaurantes.core.views.index'),
    url(r'^cadastro/$', 'restaurantes.core.views.cadastro'),
    url(r'^pratos/$', 'restaurantes.core.views.pratos'),
    url(r'^login/$', 'restaurantes.core.views.login'),
    url(r'^carrinho/$', 'restaurantes.core.views.carrinho'),
    url(r'^pratos/carrinho$', 'restaurantes.core.views.adicionar_pratos_carrinho'),
)
