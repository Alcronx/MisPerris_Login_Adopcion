from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^formulario/',views.pagina_formulario, name='pagina_formulario'),
    url(r'^rescatado/',views.nuevo_rescatado, name='nuevo_rescatado'),
]