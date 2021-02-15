from django import forms
from django.forms import ModelForm
from Ask_the_doctor.models import answers_from_therapist
from ckeditor.widgets import CKEditorWidget
class AnswerForm(forms.ModelForm):

   
	answer=forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control','placeholder': 'Type here'}))

	class Meta:
		model=answers_from_therapist
		fields=['answer']

class AnswerUpdateForm(forms.ModelForm):
	answer=forms.CharField(widget=CKEditorWidget(attrs={'class':'form-control','placeholder':'Type here'}))
	class Meta:
		model=answers_from_therapist
		fields=['answer']