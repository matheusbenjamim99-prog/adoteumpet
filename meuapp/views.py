from django.shortcuts import render
from django.shortcuts import render
from .models import Cachorro
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CachorroForm
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, 'index.html')

def project(request):

    # Captura os filtros enviados pelo <select>
    especie = request.GET.get("especie")
    porte = request.GET.get("porte")
    idade = request.GET.get("idade")

    # Busca todos os registros
    cachorro = Cachorro.objects.all()

    # Aplica filtros se o usuário escolher algo
    if especie and especie != "all":
        cachorro = cachorro.filter(especie=especie)

    if porte and porte != "all":
        cachorro = cachorro.filter(porte=porte)

    # Se não existir nenhum registro, apenas renderiza a página
    if not cachorro.exists():
        return render(request, "project.html", {"cachorro": []})

    return render(request, "project.html", {"cachorro": cachorro})

def sponsorship(request):
    cachorro = Cachorro.objects.all()
    
    if not Cachorro.objects.exists():
        return render(request, 'sponsorship.html')
    else:
        return render(request, 'sponsorship.html', {'cachorro' : cachorro})

def success(request):
    cachorro = Cachorro.objects.all()
    if not Cachorro.objects.exists():
        return render(request, 'sponsorship.html')
    else:
        return render(request, 'success_stories.html', {'cachorro' : cachorro})

def contact(request):
    return render(request, 'contact.html')

@login_required
def cadastrar_animal(request):
    if request.method == 'POST':
        form = CachorroForm(request.POST, request.FILES)
        if form.is_valid():
            cachorro = form.save(commit=False)
            cachorro.usuario = request.user 
            cachorro.save()
            return redirect('painel')
    else:
        form = CachorroForm()

    return render(request, 'cadastro_animal.html', {'form': form})

@login_required
def painel(request):
    cachorros = Cachorro.objects.filter(usuario=request.user)

    return render(request, 'painel.html', {'cachorros': cachorros})

@login_required
def editar_animal(request, id):
    cachorro = get_object_or_404(Cachorro, id=id, usuario=request.user)

    if request.method == 'POST':
        form = CachorroForm(request.POST, request.FILES, instance=cachorro)
        if form.is_valid():
            form.save()
            return redirect('painel')
    else:
        form = CachorroForm(instance=cachorro)

    return render(request, 'editar_animal.html', {'form': form})