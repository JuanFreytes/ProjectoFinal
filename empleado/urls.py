from django.urls import path

from empleado import views


app_name='empleado'
urlpatterns = [
    path('empleados', views.EmpleadoListView.as_view(), name='empleado-list'),
    path('empleado/add/', views.EmpleadoCreateView.as_view(), name='empleado-add'),
    path('empleado/<int:pk>/detail', views.EmpleadoDetailView.as_view(), name='empleado-detail'),
    path('empleado/<int:pk>/update', views.EmpleadoUpdateView.as_view(), name='empleado-update'),
    path('empleado/<int:pk>/delete', views.EmpleadoDeleteView.as_view(), name='empleado-delete'),
]
