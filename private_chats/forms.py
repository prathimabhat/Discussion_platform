from django import forms
from django.forms import ModelForm
from .models import PersonalMessages,GroupMessages,Group
from accounts.models import Profile

class TxtForm(forms.ModelForm):
	message=forms.CharField(label='',widget=forms.Textarea(attrs={'class':'form-control',
		'placeholder':'Type here...',
		'rows':'1',
		'cols':'70',
		'border-radius':'5px'
		}))

	class Meta:
		model=PersonalMessages
		fields=['message']
class NewGroupForm(forms.ModelForm):
	name=forms.CharField(label='',widget=forms.TextInput(attrs={
		'class':'form-control',
		'placeholder':'Give a name to your group'
		}))
	members=forms.ModelMultipleChoiceField(queryset=Profile.objects.filter(superuser=False),widget=forms.CheckboxSelectMultiple,required=True)
	class Meta:
		model=Group
		fields=['name','members']

class GrpForm(forms.ModelForm):
	content=forms.CharField(label='Group name',widget=forms.Textarea(attrs={'class':'form-control',
		'placeholder':'Type here...',
		'rows':'1',
		'cols':'70',
		'border-radius':'5px'
		}))
	class Meta:
		model=GroupMessages
		fields=['content']