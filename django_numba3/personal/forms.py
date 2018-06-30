from django import forms
from personal.models import Stories

class StoriesForm(forms.Form):
	title = forms.CharField()
	body = forms.CharField()