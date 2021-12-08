from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import Registro, Area
from directorio.models import Encargado
from expediente.models import Compra, Almacen
from galeria.models import Foto
from politicas.models import Contenido


# Create your views here.
class IndexView(TemplateView):
    model = Area
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Area'
        context['areaList'] = Area.objects.all()
        return context
