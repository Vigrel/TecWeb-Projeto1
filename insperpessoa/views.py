from django.shortcuts import render, redirect
from .models import Insperpessoa

def index(request):
    if request.method == 'POST':
        nome = request.POST.get('nome');
        sobrenome = request.POST.get('sobrenome');
       
        pessoa = Insperpessoa(nome = nome, sobrenome = sobrenome);
        pessoa.save();
        return redirect('index');

    else:
        cadastrados = Insperpessoa.objects.all()
        num_cadastrados = Insperpessoa.objects.count()
        pessoas = [cadastrados, num_cadastrados]
        return render(request, 'insperpessoa/index.html', {'pessoas': pessoas})
