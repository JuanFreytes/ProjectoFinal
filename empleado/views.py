
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from empleado.models import Empleado

class EmpleadoListView(ListView):
    model = Empleado
    template_name = "empleado/empleado_list.html"


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleado/empleado_detail.html"


class EmpleadoCreateView(LoginRequiredMixin, CreateView):
    model = Empleado
    success_url = reverse_lazy('empleado:empleado-list')
    fields = '__all__'


class EmpleadoUpdateView(LoginRequiredMixin, UpdateView):
    model = Empleado
    success_url = reverse_lazy('empleado:empleado-list')
    fields = '__all__'


class EmpleadoDeleteView(LoginRequiredMixin, DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleado:empleado-list')
