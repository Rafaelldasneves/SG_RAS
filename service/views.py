from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.contrib import messages


class PeriodListView(TemplateView):
    template_name= 'list_period.html'