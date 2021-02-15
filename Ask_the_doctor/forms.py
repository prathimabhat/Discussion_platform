from django import forms
from django.forms import ModelForm
from .models import question_to_therapist
from ckeditor.widgets import CKEditorWidget
#from therapist_dashboard.models import Patients
class QuestionForm(forms.ModelForm):
    
	question=forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control','placeholder': 'Type here'}))

	class Meta:
		model=question_to_therapist
		fields=['question']
		'''widgets={

	    		'question':forms.Textarea(attrs={'class':'form-control','label':'question','placeholder': 'Type here...'})
	    	}'''

   
class QuestionUpdateForm(forms.ModelForm):
	question=forms.CharField(widget=CKEditorWidget(attrs={'class':'form-control','placeholder':'Type here'}))
	class Meta:
		model=question_to_therapist
		fields=['question']

'''class PatientForm(forms.ModelForm):
	name=forms.CharField(widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder':'Enter your name',
		'size':'40'
		}))

	address=forms.CharField(widget=forms.Textarea(attrs={
		'class':'form-control',
		'placeholder':'Enter your address',
		'rows':'2',
		'cols':'70'
		}))
	mental_illness=forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control',
		'placeholder':'Enter the name of the mental illness you are suffering from. If you do not know, type "Do not know"',
		'size':'40'
		}))

	date_of_birth = forms.DateField(label='Enter your date of birth',widget=forms.DateTimeInput(attrs=
		{'placeholder': 'YYYY-MM-DD',
		'size':'40',
		'class':'datetime-input'
		}))
	gender_choices=[
		('MALE','Male'),
		('FEMALE','Female'),
		('OTHERS','Others'),
		('NOTDISCLOSE','I do not wish to disclose')

	]
	gender=forms.CharField(max_length=2,widget=forms.Select(choices=gender_choices))

	class Meta:
		model=Patients
		fields=['name','gender','date_of_birth','address','mental_illness']
'''