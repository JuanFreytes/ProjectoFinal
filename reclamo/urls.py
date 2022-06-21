from django.urls import path

from reclamo import views


app_name='reclamo'
urlpatterns = [
    path('reclamos', views.ReclamoListView.as_view(), name='reclamo-list'),
    path('reclamo/add/', views.ReclamoCreateView.as_view(), name='reclamo-add'),
    path('reclamo/<int:pk>/detail', views.ReclamoDetailView.as_view(), name='reclamo-detail'),
    path('reclamo/<int:pk>/update', views.ReclamoUpdateView.as_view(), name='reclamo-update'),
    path('reclamo/<int:pk>/delete', views.ReclamoDeleteView.as_view(), name='reclamo-delete'),
]
