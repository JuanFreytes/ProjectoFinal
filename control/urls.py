from django.urls import path

from control import views


app_name='control'
urlpatterns = [
    path('controles', views.controles, name='control-list'),
    path('control/add', views.control_form, name='control-add'),
    path('control/<int:pk>/delete', views.delete_control, name='control-delete'),
]
