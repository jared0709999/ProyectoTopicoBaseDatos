from typing import AsyncIterable
from django.shortcuts import render
from django.views.generic import TemplateView
# Importar el modelo
from galeria.models import Foto


# Create your views here.
class GaleriaView(TemplateView):
    model = Foto
    template_name = 'galeria.html'

    def get_context_data(self, **kwargs):
        context = super(GaleriaView, self).get_context_data(**kwargs)
        context['title'] = 'Galeria'
        context['galeriaList'] = Foto.objects.all()
        return context
