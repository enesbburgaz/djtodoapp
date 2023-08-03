from django import forms
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Todo

class TodoForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = 'add'
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit','Save'))
    
    STATUS_CHOICES=(
    ("in","InProgress"),
    ("bl","Blocked"),
    ("co","Completed"),
    ("ca","Cancelled"),
    )
    
    title = forms.CharField()
    description = forms.CharField()
    status = forms.ChoiceField(choices=STATUS_CHOICES)
    