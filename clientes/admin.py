from django.contrib import admin
from clientes.models import Cliente, Cartao, Prato, Pedido

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Cartao)
admin.site.register(Prato)
admin.site.register(Pedido)
