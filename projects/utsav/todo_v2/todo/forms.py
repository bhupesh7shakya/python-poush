from django import forms
class TaskForm(forms.Form):
    title = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control'
                })
            , label = "Task title")
    description = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control'}), label = "Descripion")
    status = forms.BooleanField(label="Completed", required=False)

class SearchBox(forms.Form):
    term = forms.CharField(widget=forms.TextInput(attrs = {'class': 'form-control'}), label="")
