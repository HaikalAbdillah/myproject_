from django.forms import ModelForm
from django import forms
from menu.models import Produk

class FormParfum(ModelForm):
    class Meta:
        model = Produk
        fields = '__all__'

        widgets = {
            'namaProduk' : forms.TextInput({'class':'form-control'}),
            'harga' : forms.TextInput({'class':'form-control'}),
            'alco' : forms.TextInput({'class':'form-control'}),
            'perML' : forms.NumberInput({'class':'form-control'}),
            'kategori_id' : forms.Select({'class':'form-control'}),
            
        }