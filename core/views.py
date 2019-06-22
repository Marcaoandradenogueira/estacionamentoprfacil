from django.shortcuts import render, redirect
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista
)

from .forms import (
    VeiculoForm,
    PessoaForm,
    MensalistaForm,
    MovRotativoForm,
    MovMensalistaForm
)


def home(request):
    context = {'mensagem':'Ola Mundo'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas':pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)


def pessoa_nome(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)

def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm_pessoa.html', {'pessoa': pessoa})


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form':form}
    return render(request, 'core/lista_veiculos.html', data)

def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')

def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)


def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm_veiculo.html', {'veiculo': veiculo})

def lista_mov_rotativos(request):
    movrotativos = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'movrotativos': movrotativos, 'form':form}
    return render(request, 'core/lista_mov_rotativos.html', data)

def mov_rotativos_novo(request):
    form = MovRotativoForm(request.POST or None)
    print('passei')
    if form.is_valid():
        print('passei')
        form.save()
    return redirect('core_lista_movrotativos')

def mov_rotativos_update(request, id):
    data = {}
    movrotativo = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=movrotativo)
    data['movrotativo'] = movrotativo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/update_movrotativos.html', data)

def mov_rot_delete(request, id):
    movrotativos = MovRotativo.objects.get(id=id)
    if request.method == 'POST':
        movrotativos.delete()
        return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/delete_confirm_movrotativos.html', {'movrotativos': movrotativos})

def lista_mensalista(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas': mensalistas, 'form':form}
    return render(request, 'core/lista_mensalistas.html', data)

def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalista')

def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/update_mensalista.html', data)

def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/delete_confirm_mensalista.html', {'mensalista': mensalista})

def lista_mov_mensalistas(request):
    movmensalistas = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data =  {'form': form, 'movmensalistas': movmensalistas}
    return render(request, 'core/lista_mov_mensalistas.html' , data)

def mov_mensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalistas')

def mov_mensalista_update(request, id):
    data = {}
    movmensalistas = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=movmensalistas)
    data['movmensalistas'] = movmensalistas
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/update_movmensalista.html', data)


def mov_mensalista_delete(request, id):
    movmensalistas = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        movmensalistas.delete()
        return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/delete_confirm_movmensalista.html', {'movmensalistas': movmensalistas})
