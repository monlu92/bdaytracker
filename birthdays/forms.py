from django import forms

from .models import Birthday


class BirthdayForm(forms.ModelForm):
    bday_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-group',
            'placeholder': "Enter person's name",
        }
    ), required=True)
    bday_date = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-group',
            'placeholder': "Enter person's birthday",
        }
    ), required=True)

    class Meta:
        model = Birthday
        fields = ('bday_name', 'bday_date',)