from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from restaurantes.core.models import Cliente, Prato, Carrinho
from restaurantes.core.forms import ClienteForm, LoginForm, CarrinhoForm

def index(request):
    return HttpResponse('Restaurantes')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        try:
            cliente = Cliente.objects.get(email=email, senha=senha)
            return HttpResponseRedirect('/pratos')
        except Cliente.DoesNotExist:
            #raise ValueError("Usuario ou senha incorretos")
            return HttpResponseRedirect('/login')
    else:
        form = LoginForm()

        return render(request, 'login.html', { 'form' : form })

def cadastro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            return HttpResponseRedirect('/login')
    else:
        form = ClienteForm()

    return render(request, 'cadastro.html', { 'form' : form })

#add login required
def pratos(request):
    pratos = Prato.objects.all().order_by('preco')
    return render(request, 'pratos.html', { 'pratos' : pratos })

def carrinho(request):
    items = Carrinho.objects.all().order_by('quantidade')
    for item in items:
        item.total = item.prato.preco * item.quantidade

    return render(request, 'carrinho.html', { 'items' : items })

#check if exists
def adicionar_pratos_carrinho(request):
    if request.method == 'POST':
        form = CarrinhoForm(request.POST)
        if form.is_valid():
            item = form.save()
            return HttpResponseRedirect('/carrinho')
    else:
        form = CarrinhoForm()

        return render(request, 'pratos_carrinho.html', { 'form' : form })
