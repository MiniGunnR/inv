from django.shortcuts import render, reverse
from django.views import generic
from django.db import transaction

from .models import LC, YarnRcv

from .forms import LC_Formset


class LCCreateView(generic.CreateView):
  model = LC
  fields = ['date', 'number', 'spinning_mill']
  template_name = 'inv/lc_form.html'

  def get_success_url(self):
    return reverse('inv:lc_updateview', args=[self.object.pk])

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


class LCUpdateView(generic.UpdateView):
  model = LC
  fields = ['date', 'number', 'spinning_mill']
  template_name = 'inv/lc_form.html'

  def get_success_url(self):
    return reverse('inv:lc_updateview', args=[self.object.pk])

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    if self.request.POST:
      context['lc_items'] = LC_Formset(self.request.POST, instance=self.object)
    else:
      context['lc_items'] = LC_Formset(instance=self.object)
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


class LCListView(generic.ListView):
  model = LC
  template_name = 'inv/lc_list.html'


class YarnRcvCreateView(generic.CreateView):
  model = YarnRcv
  fields = ['lc_item', 'date', 'challan_no', 'lot', 'quantity_rcv']
  template_name = 'inv/yarn_rcv_form.html'
