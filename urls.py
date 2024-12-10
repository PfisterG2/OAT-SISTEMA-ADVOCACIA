from django.contrib import admin
from django.urls import path, include

# Importações das views de cada app
from clientes import views as clientes_views
from agenda import views as agenda_views
from financeiro import views as financeiro_views
from processos import views as processos_views
from advogados import views as advogados_views
from documentos import views as documentos_views  # Certifique-se de importar as views de documentos

# Importando a view para a página inicial (home)
from . import views  # Aqui você importa a view home

from rest_framework.routers import DefaultRouter
from documentos.views import DocumentoViewSet  # Importa o viewset para documentos
from .views import ClienteViewSet
from advogados.views import AdvogadoViewSet
# Criação do router para a API
router = DefaultRouter()
router.register(r'documentos', DocumentoViewSet)

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)

router = DefaultRouter()
router.register(r'advogados', AdvogadoViewSet, basename='advogado')
urlpatterns = [
    path('admin/', admin.site.urls),  # URL para o admin
    path('clientes/', clientes_views.index, name='clientes_index'),  # Página de clientes
    path('financeiro/', financeiro_views.index, name='financeiro'),  # Página financeira
    path('processos/', processos_views.processos, name='processos'),  # Página de processos
    path('agenda/', agenda_views.agenda, name='agenda'),  # Página da agenda
    path('documentos/', documentos_views.documentos, name='lista_documentos'),  # Página de documentos
    path('api/', include(router.urls)),  # Incluindo as rotas da API de advogados
    path('', views.home, name='home'),  # Página inicial
]
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)