from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages


class Home(TemplateView):
    template_name = 'home.html'
    
    # def get(self, request,):
    #         messages.info(request, 'PAGINA CARREGADA COM SUCESSO !')
    #         return super().get(request,)