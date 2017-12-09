from django.shortcuts import render, reverse
from django.views import generic
from django.db import transaction

from .models import LC, LCItem

from .forms import LC_Formset


class LCCreateView(generic.CreateView):
    model = LC
    fields = ['date', 'number', 'spinning_mill']
    template_name = 'inv/lc_form.html'

    def get_success_url(self):
        return reverse('inv:lc_createview')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['lc_items'] = LC_Formset(self.request.POST)
        else:
            context['lc_items'] = LC_Formset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        lc_items = context['lc_items']
        with transaction.atomic():
            self.object = form.save()
            if lc_items.is_valid():
                lc_items.instance = self.object
                lc_items.save()
        return super().form_valid(form)

