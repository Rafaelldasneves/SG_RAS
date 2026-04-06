from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from . import models

from django.contrib.auth import get_user_model
User = get_user_model()

from accounts.forms import RegisterForm


class RegisterUserView(CreateView):
    model = User
    template_name = 'registration/register_servidor.html'
    form_class = RegisterForm
    success_url = reverse_lazy ('login')
    success_message = " Usuário cadastrado com sucesso !"

    def form_valid(self, form):
        form.instance.password = make_password(form.instance.password)
        form.save()
        messages.success(self.request, self.success_message)
        return super(RegisterUserView, self).form_valid(form)


class ListServidor(ListView):
    model = models.CustomUser
    template_name = 'list_servidor.html'
    context_object_name = "servidores"


class DetailServidor(DetailView):
    model = models.CustomUser
    template_name = 'detail_servidor.html'


class UpdateServidor(UpdateView):
    model = models.CustomUser
    template_name= 'update_servidor.html'
    form_class = RegisterForm
    success_url = reverse_lazy ('list_servidor')


class DeleteServidor(DeleteView):
    model = models.CustomUser
    template_name = 'delete_servidor.html'
    context_object_name = 'servidor'
    success_url = reverse_lazy ('list_servidor')