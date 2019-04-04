from django import forms
from .models import Staff, Post

class StaffForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'on', 'autocomplete':'off', 'class':'form-control', 'placeholder':'Name'}))

	salary = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Salary'}))
	mobile = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile'}))
	email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
	address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}))

	def clean_mobile(self):
		mobile=self.cleaned_data.get('mobile')
		try:
			if len(mobile)>0:
				a=int(mobile)
		except:
			raise forms.ValidationError("Incorrect mobile number")
		if len(mobile)>0 and len(mobile)!=10:
			raise forms.ValidationError("Incorrect mobile number")

		return mobile

	class Meta:
		model=Staff
		fields=['name', 'post', 'salary', 'mobile', 'email', 'address']


class PostForm(forms.ModelForm):
	post_type = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Post type'}))
	class Meta:
		model = Post
		fields = ['post_type']



