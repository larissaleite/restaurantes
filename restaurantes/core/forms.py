from django.forms import ModelForm
from django import forms
from restaurantes.core.models import Cliente, Carrinho

class ClienteForm(ModelForm):
    class Meta:
        senha = forms.CharField(widget=forms.PasswordInput)
        model = Cliente
        widgets = {
            'senha': forms.PasswordInput(),
        }

class LoginForm(ModelForm):
    class Meta:
        senha = forms.CharField(widget=forms.PasswordInput)
        model = Cliente
        widgets = {
            'senha': forms.PasswordInput(),
        }
        exclude = ('nome', 'endereco', 'telefone')

class CarrinhoForm(ModelForm):
    class Meta:
        model = Carrinho
