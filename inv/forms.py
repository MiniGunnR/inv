from django import forms
from django.forms import inlineformset_factory

from .models import LC, LCItem


class LCItemForm(forms.ModelForm):
    class Meta:
        model = LCItem
        fields = ['count', 'composition', 'quantity', 'unit']

LC_Formset = inlineformset_factory(LC, LCItem, form=LCItemForm, extra=1)
