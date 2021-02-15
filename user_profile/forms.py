from django import forms
from django.forms import ModelForm
from community_forum.models import Answers,Questions
from ckeditor.widgets import CKEditorWidget

class QuestionUpdateForm(forms.ModelForm):
	question_title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Give a title to your question'}))
	question_detail=forms.CharField(widget=CKEditorWidget(attrs={'class':'form-control','placeholder':'Type here'}))
	class Meta:
		model=Questions
		fields=['question_title','question_detail']

class AnswerUpdateForm(forms.ModelForm):

	answer=forms.CharField(widget=CKEditorWidget(attrs={'class':'form-control','placeholder':'Type here'}))
	class Meta:
		model=Answers
		fields=['answer']