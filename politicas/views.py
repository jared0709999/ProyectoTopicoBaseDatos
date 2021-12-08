from typing import AsyncIterable
from django.shortcuts import render
from django.views.generic import TemplateView
# Importar el modelo
from politicas.models import Contenido


# Create your views here.

class PoliticasView(TemplateView):
    model = Contenido
    template_name = 'politicas.html'

    def get_context_data(self, **kwargs):
        context = super(PoliticasView, self).get_context_data(**kwargs)
        context['title'] = 'Politicas'
        context['politicasList'] = Contenido.objects.all()
        return context
