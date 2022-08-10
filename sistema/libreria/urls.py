from django.urls import URLPattern, path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('valijas', views.valijas, name='valijas'),
    path('valijas/crear', views.crear, name='crear'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('valijas/editar/<int:id>', views.editar, name='editar'),
    
    
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
