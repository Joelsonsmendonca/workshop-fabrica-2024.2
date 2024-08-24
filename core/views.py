from django.shortcuts import render

def index(request):
    context = {
        'curso' : 'programação web'
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')