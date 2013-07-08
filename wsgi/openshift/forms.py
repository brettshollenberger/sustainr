from django import forms
from django.forms.widgets import SelectMultiple

class CollegeSelect(forms.Form):
    college1 = forms.CharField()
    college2 = forms.CharField()
    scope1 = forms.BooleanField(required=False)
    scope2 = forms.BooleanField(required=False)
    scope3 = forms.BooleanField(required=False)
    offsets = forms.BooleanField(required=False)
    builtspace = forms.BooleanField(required=False)
    studentfte = forms.BooleanField(required=False)
