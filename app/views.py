from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from accounts import models


class Home(TemplateView):
    template_name = 'home.html'
    
    # def get(self, request,):
    #         messages.info(request, 'PAGINA CARREGADA COM SUCESSO !')
    #         return super().get(request,)
