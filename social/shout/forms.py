# shout/forms.py
from django import forms
from .models import shout

class ShoutForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
        attrs={
                "placeholder": "Shout something...",
                "class": "textarea is-success is-large",
            }
        ),
        label="",
    )
    class Meta:
        model = shout
        exclude = ("user", )