from django import forms
from .models import DataCollection

class DataForm(forms.ModelForm):
    data=forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10, 'placeholder':'Teach me!'}),
    label='', max_length=500)

    class Meta:
        model=DataCollection
        fields=('data',)
