from django.urls import path

from cliente import views


app_name='cliente'
urlpatterns = [
    path('clientes', views.cliente_list, name='cliente-list'),
    path('cliente/add', views.cliente_form, name='cliente-add'),
    path('cliente/<int:pk>/update', views.update_cliente, name='cliente-update'),
    path('cliente/<int:pk>/delete', views.delete_cliente, name='cliente-delete'),
]
