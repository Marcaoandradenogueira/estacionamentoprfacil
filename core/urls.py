from django.conf.urls import url, include
from django.urls import path
from core.views import (
    home, 
    lista_pessoas, 
    lista_veiculos, 
    lista_mov_rotativos,
    lista_mensalista,
    lista_mov_mensalistas,
    pessoa_nome,
    veiculo_novo,
    mensalista_novo,
    mov_rotativos_novo,
    mov_mensalista_novo,
    pessoa_update,
    veiculo_update,
    mov_rotativos_update,
    mensalista_update,
    mov_mensalista_update,
    pessoa_delete,
    veiculo_delete,
    mov_rot_delete,
    mensalista_delete,
    mov_mensalista_delete
)

urlpatterns = [
    path('', home, name='home'),
    path('pessoa/', lista_pessoas, name='core_lista_pessoas'),
    path('pessoa_novo/', pessoa_nome, name='core_lista_pessoa_nome'),
    path('pessoa_update/<int:id>/', pessoa_update, name='core_pessoa_update'),
    path('pessoa_delete/<int:id>/', pessoa_delete, name='core_pessoa_delete'),

    path('veiculo/', lista_veiculos, name='core_lista_veiculos'),
    path('veiculo_novo/', veiculo_novo, name='core_veiculo_novo'),
    path('veiculo_update/<int:id>/', veiculo_update, name='core_veiculo_update'),
    path('veiculo_delete/<int:id>/', veiculo_delete, name='core_veiculo_delete'),

    path('mov_rot_list/', lista_mov_rotativos, name='core_lista_movrotativos'),
    path('mov_rot_novo/', mov_rotativos_novo, name='core_movrotativos_novo'),
    path('mov_rot_update/<int:id>/', mov_rotativos_update, name='core_movrotativos_update'),
    path('mov_rot_delete/<int:id>/', mov_rot_delete, name='mov_rot_delete'),

    path('mensalista/', lista_mensalista, name='core_lista_mensalista'),
    path('mensalista_novo/', mensalista_novo, name='core_mensalista_novo'),
    path('mensalista_update/<int:id>/', mensalista_update, name='core_mensalista_update'),
    path('mensalista_delete/<int:id>/', mensalista_delete, name='core_mensalista_delete'),

    path('mov_mensalista_list/', lista_mov_mensalistas, name='core_lista_movmensalistas'),
    path('mov_mensalista_novo/', mov_mensalista_novo, name='core_movmensalistas_novo'),
    path('mov_mensalista_update/<int:id>/', mov_mensalista_update, name='core_movmensalistas_update'),
    path('mov_mensalista_delete/<int:id>/', mov_mensalista_delete, name='core_movmensalistas_delete'),
]