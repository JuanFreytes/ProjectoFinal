
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from reclamo.models import Reclamo

class ReclamoListView(ListView):
    model = Reclamo
    template_name = "reclamo/reclamo_list.html"


class ReclamoDetailView(DetailView):
    model = Reclamo
    template_name = "reclamo/reclamo_detail.html"
    fields = ['nombre', 'telefono', 'fecha','planta', 'descripcion']


class ReclamoCreateView(LoginRequiredMixin, CreateView):
    model = Reclamo
    success_url = reverse_lazy('reclamo:reclamo-list')
    fields = ['nombre', 'telefono','fecha','planta', 'descripcion']


class ReclamoUpdateView(LoginRequiredMixin, UpdateView):
    model = Reclamo
    success_url = reverse_lazy('reclamo:reclamo-list')
    fields = ['nombre', 'telefono','fecha','planta', 'descripcion']


class ReclamoDeleteView(LoginRequiredMixin, DeleteView):
    model = Reclamo
    success_url = reverse_lazy('reclamo:reclamo-list')
