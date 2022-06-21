from django import forms


class ControlForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre del Responsable')
    due_date = forms.DateField(
        label='Fecha de Realización',
        widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})
    )
    is_delivered = forms.BooleanField(label='Están todos los Reclamos Resueltos?', required=False)
