from django import forms

class ClienteForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre')
    address = forms.CharField(max_length=40, label='Dirección')
    email = forms.EmailField(label='Correo electrónico')
    telefono = forms.CharField(max_length=40, label='Telefono')
    
