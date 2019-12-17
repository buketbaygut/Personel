from django import forms
from .models import Personel

class PersonelForm(forms.ModelForm):
    class Meta:
        model = Personel
        fields = '__all__'
        widgets={'id':forms.HiddenInput()}