from django import forms

class ListForm(forms.Form):
    text = forms.CharField(max_length=50, label='item')
    # widget=forms.TextInput(attrs=
    # {
    #     'class': 'form-control',
    #     'placeholder': 'A Django ToDo List',
    # })
    