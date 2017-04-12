from django import forms
from .models import SavedText

class NotesForm(forms.ModelForm):
    ENGLSIH = "en"
    MANDARIN = "zh-CN"
    LANG_CHOICES = (
        (ENGLSIH, 'English'),
        (MANDARIN, 'Mandarin'),
    )
    #user = user.request()
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-4'}))
    lang = forms.ChoiceField(choices=LANG_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control col-md-4', 'id': 'selectpicker'}))
    class Meta:
        model = SavedText
        fields = ['text', 'lang']
