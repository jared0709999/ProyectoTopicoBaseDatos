from typing import AsyncIterable
from django.shortcuts import render
from django.views.generic import TemplateView
# Importar el modelo
from expediente.models import Almacen


# Create your views here.

class ExpedienteView(TemplateView):
    model = Almacen
    template_name = 'expediente.html'

    def get_context_data(self, **kwargs):
        context = super(ExpedienteView, self).get_context_data(**kwargs)
        context['title'] = 'Expediente'
        context['expedienteList'] = Almacen.objects.all()
        return context
