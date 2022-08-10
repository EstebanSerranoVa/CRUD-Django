from attr import field
from django import forms
from .models import Valija

class ValijaForm(forms.ModelForm):
    class Meta:
        model = Valija
        fields = '__all__'