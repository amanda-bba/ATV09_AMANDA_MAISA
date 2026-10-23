# portal/models.py

from django.db import models

class Conteudo(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    conteudo_html = models.TextField(help_text="Insira apenas o HTML interno do conteúdo.")
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Menu(models.Model):
    TIPO_DESTINO_CHOICES = [
        ('interno', 'Conteúdo Interno'),
        ('externo', 'Link Externo'),
    ]

    titulo = models.CharField(max_length=50)
    tipo_destino = models.CharField(max_length=10, choices=TIPO_DESTINO_CHOICES, default='interno')
    conteudo_relacionado = models.ForeignKey(
        Conteudo, on_delete=models.SET_NULL, null=True, blank=True, related_name='itens_menu'
    )
    url_externa = models.URLField(max_length=200, blank=True, null=True)
    ordem = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return self.titulo
