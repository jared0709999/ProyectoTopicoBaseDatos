from django.contrib import admin
from django.urls import path, include
from frontend.views import IndexView
from expediente.views import ExpedienteView
from politicas.views import PoliticasView
from directorio.views import DirectorioView
from galeria.views import GaleriaView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from core import views
from directorio.models import *
from expediente.models import*
from galeria.models import*
from politicas.models import*
# Agregar las vistas de directorio

router = routers.DefaultRouter()
router.register(r'Users', views.UserViewSet)
router.register(r'Groups', views.GroupViewSet)
router.register(r'Area', views.AreaViewSet)
router.register(r'Registro', views.RegistroViewSet)
router.register(r'Encargado', views.EncargadoViewSet)
router.register(r'Compra', views.CompraViewSet)
router.register(r'Foto', views.FotoViewSet)
router.register(r'Contenido', views.ContenidoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name= 'index'),
    path('directorio/', DirectorioView.as_view(), name='directorio'),
    path('expediente/', ExpedienteView.as_view(), name='expediente'),
    path('galeria/', GaleriaView.as_view(), name='galeria'),
    path('politicas/', PoliticasView.as_view(), name='politicas'),

    # Agregar ruta para vista directorio
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)