from django import forms

class NoteForm(forms.Form):
    nota = forms.CharField(label='Nota', max_length=100)
