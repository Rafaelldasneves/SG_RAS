from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from . import models, forms


class ServiceCreateView(CreateView):
    model = models.Service
    template_name = 'create_service.html'
    form_class = forms.ServiceForms
    success_url = reverse_lazy ('list_services')


class ServiceListView(ListView):
    model = models.Service
    template_name = "list_services.html"
    context_object_name = "service"
    

class ServiceUpdateView(UpdateView):
    model = models.Service
    template_name = 'update_service.html'
    form_class = forms.ServiceForms
    success_url = reverse_lazy ('list_services')
    context_object_name = "service"


class ServiceDeleteView(DeleteView):
    model = models.Service
    template_name = 'delete_service.html'
    success_url = reverse_lazy ('list_services')
    context_object_name = "service"