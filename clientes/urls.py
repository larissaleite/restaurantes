from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'restaurantes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'clientes.views.index'),
    url(r'^cadastro/$', 'clientes.views.cadastro'),
)
