from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from . import models, forms


class PeriodListView(ListView):
    model = models.Period
    template_name = "list_periods.html"
    context_object_name = "periods"

    def get_queryset(self):
        queryset = super().get_queryset()
        date_start = self.request.GET.get('date_start')

        if date_start:
            queryset = queryset.filter(date_start__icontains=date_start)

        return queryset 


class PeriodCreateView(CreateView):
    model = models.Period
    template_name = 'create_period.html'
    form_class = forms.PeriodForms
    success_url = reverse_lazy ('list_periods')


class PeriodDetailView(DetailView):
    model = models.Period
    template_name = 'detail_period.html'


class PeriodUpdateView(UpdateView):
    model = models.Period
    template_name = 'update_period.html'
    form_class = forms.PeriodForms
    success_url = reverse_lazy ('list_periods')


class PeriodDeleteView(DeleteView):
    model = models.Period
    template_name = 'delete_period.html'
    success_url = reverse_lazy ('list_periods')