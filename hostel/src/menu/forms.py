from django import forms
from .models import Item, Timing

class MenuUpdateForm(forms.ModelForm):
	day = forms.CharField(label="Day",widget=forms.TextInput(attrs={'autofocus':'on', 'autocomplete':'off', 'class':'form-control', 'placeholder':'Day'}))

	breakfast = forms.CharField(label='BreakFast', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'BreakFast'}))

	lunch = forms.CharField(label='Lunck', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'BreakFast'}))
	evening = forms.CharField(label='Evening', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Lunch'}))
	dinner = forms.CharField(label='Dinner', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Dinner'}))
	

	class Meta:
		model=Item
		fields=['day', 'breakfast', 'lunch', 'evening', 'dinner']

class TimingUpdateForm(forms.ModelForm):
	breakfast_time = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'on', 'autocomplete':'off', 'class':'form-control'}))
	lunch_time = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control'}))
	evening_time = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control'}))
	dinner_time = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control'}))
	class Meta:
		model=Timing
		fields=['breakfast_time','lunch_time','evening_time','dinner_time']
