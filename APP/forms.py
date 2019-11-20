from django import forms
from .models import Bonzai


class BonzaiForm(forms.ModelForm):
    class Meta:
        model = Bonzai
        fields = '__all__'