from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from clientes.models import Cliente, Prato
from clientes.forms import ClienteForm

def index(request):
    return HttpResponse('Restaurantes')

def cadastro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            return HttpResponseRedirect('/')
    else:
        form = ClienteForm()

    return render(request, 'cadastro.html', { 'form' : form })

#add login required
def pratos(request):
    pratos = Prato.objects.all().order_by('preco')
    return render(request, 'pratos.html', { 'pratos' : pratos })
