from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.contrib import messages

from django.contrib.auth import get_user_model
User = get_user_model()

from accounts.forms import RegisterForm


class RegisterUserView(CreateView):
    model = User
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy ('login')
    success_message = " Usuário cadastrado com sucesso !"

    def form_valid(self, form):
        form.instance.password = make_password(form.instance.password)
        form.save()
        messages.success(self.request, self.success_message)
        return super(RegisterUserView, self).form_valid(form)
