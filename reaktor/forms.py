from django import forms

class TomlForm(forms.Form):
    file = forms.FileField()