import random
import string
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.shortcuts import render

from cliente.models import Cliente
from cliente.forms import ClienteForm


def cliente_list(request):
    clientes = Cliente.objects.all()

    context_dict = {
        'clientes': clientes
    }

    return render(
        request=request,
        context=context_dict,
        template_name="cliente/cliente_list.html"
    )


@login_required
def cliente_form(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            data = cliente_form.cleaned_data
            cliente = Cliente(
                name=data['name'],
                address=data['address'],
                email=data['email'],
                telefono=data['telefono'],
            )
            cliente.save()

            clientes = Cliente.objects.all()
            context_dict = {
                'clientes': clientes
            }
            return render(
                request=request,
                context=context_dict,
                template_name="cliente/cliente_list.html"
            )

    cliente_form = ClienteForm(request.POST)
    context_dict = {
        'cliente_form': cliente_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='cliente/cliente_form.html'
    )


@login_required
def update_cliente(request, pk: int):
    cliente = Cliente.objects.get(pk=pk)

    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            data = cliente_form.cleaned_data
            cliente.name = data['name']
            cliente.address = data['address']
            cliente.email = data['email']
            cliente.telefono = data['telefono']
            cliente.save()

            clientes = Cliente.objects.all()
            context_dict = {
                'clientes': clientes
            }
            return render(
                request=request,
                context=context_dict,
                template_name="cliente/cliente_list.html"
            )

    cliente_form = ClienteForm(model_to_dict(cliente))
    context_dict = {
        'cliente': cliente,
        'cliente_form': cliente_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='cliente/cliente_form.html'
    )


@login_required
def delete_cliente(request, pk: int):
    cliente = Cliente.objects.get(pk=pk)
    if request.method == 'POST':
        cliente.delete()

        clientes = Cliente.objects.all()
        context_dict = {
            'clientes': clientes
        }
        return render(
            request=request,
            context=context_dict,
            template_name="cliente/cliente_list.html"
        )

    context_dict = {
        'cliente': cliente,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='cliente/cliente_confirm_delete.html'
    )
