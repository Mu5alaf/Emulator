from django import forms
from .models import App

class app_form(forms.ModelForm):
    class Meta:
        model = App
        fields = ['apk_name','apk_path']