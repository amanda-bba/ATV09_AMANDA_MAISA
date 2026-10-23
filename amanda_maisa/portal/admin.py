from django.contrib import admin
from .models import Conteudo, Menu

@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'ativo')
    prepopulated_fields = {'slug': ('titulo',)}  # Preenche o slug automaticamente ao digitar o título
    list_filter = ('ativo',)
    search_fields = ('titulo', 'conteudo_html')

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo_destino', 'ordem', 'ativo')
    list_editable = ('ordem', 'ativo')  # Permite alterar a ordem e status diretamente na listagem
    list_filter = ('tipo_destino', 'ativo')
