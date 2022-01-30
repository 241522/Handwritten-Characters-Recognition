from django import forms


class FileFieldForm(forms.Form):
    path = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
