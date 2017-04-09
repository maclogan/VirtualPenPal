from django import forms
from .models import SavedText

class NotesForm(forms.ModelForm):
    #user = user.request()
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-12'}))
    class Meta:
        model = SavedText
        fields = ['text']
