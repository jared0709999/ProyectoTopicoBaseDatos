from typing import AsyncIterable
from django.shortcuts import render
from django.views.generic import TemplateView
# Importar el modelo
from directorio.models import Encargado


# Create your views here.
class DirectorioView(TemplateView):
    model = Encargado
    template_name = 'directorio.html'

    def get_context_data(self, **kwargs):
        context = super(DirectorioView, self).get_context_data(**kwargs)
        context['title'] = 'Directorio'
        context['directorioList'] = Encargado.objects.all()
        return context
