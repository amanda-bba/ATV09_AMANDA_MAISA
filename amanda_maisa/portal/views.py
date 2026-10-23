from django.shortcuts import render, get_object_or_404
from .models import Menu, Conteudo

# Função auxiliar para buscar os itens de menu ativos ordenados
def get_menu_ativo():
    return Menu.objects.filter(ativo=True)

# View da página inicial (Capa)
def index(request):
    menu = get_menu_ativo()
    return render(request, 'portal/index.html', {'menu': menu})

# View dinâmica que busca o conteúdo interno pelo 'slug'
def exibir_conteudo(request, slug):
    menu = get_menu_ativo()
    conteudo = get_object_or_404(Conteudo, slug=slug, ativo=True)
    return render(request, 'portal/conteudo.html', {
        'menu': menu,
        'conteudo': conteudo
    })
