from django.urls import path

from pyprg.aperitivos.views import video

app_name = 'aperitivos'
urlpatterns = [
    # <slug> => pode ser definido como varios tipos
    # vamos definir como um tipo especial tipo slug que será uma string cpom caracteres pre-definido
    # que podem aparecer compondo o path do endereço deste recurso
    # parametro video será sem () pois queremos acesso direto a view de video
    path('<slug:slug>', video, name='video'),
]
