from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
	input_type='date'



class SignUpForm(UserCreationForm):
	username=forms.CharField(label=' Create a username',widget=forms.TextInput(attrs={'placeholder':'NinjaGirl','size':'40'}))
	email=forms.EmailField(label='Enter your email address',widget=forms.EmailInput(attrs={'placeholder': 'jondoe@example.com','size':'40'}))
	first_name=forms.CharField(label='Enter your first name',widget=forms.TextInput(attrs={'placeholder':'Jon','size':'40'}))
	last_name=forms.CharField(label='Enter your last name',widget=forms.TextInput(attrs={'placeholder':'Doe','size':'40'}))

	date_of_birth = forms.DateField(label='Enter your date of birth',widget=forms.DateInput(attrs={'type':'date'}))
	location=forms.CharField(label='Where are you from?',widget=forms.TextInput(attrs={'placeholder': 'eg. Bangalore,India','size':'40'}))
	reason=forms.CharField(label='Why do you want to join our community?',widget=forms.Textarea(attrs={'placeholder': 'I want to join because...','size':'45'}))
	
	password1=forms.CharField(label='Create a password',help_text='Make sure it is atleast 8 characters including a number, a special character, an uppercase and a lowercase letter',widget=forms.PasswordInput(attrs={'size':'40'}))
	password2=forms.CharField(label='Type your password again',widget=forms.PasswordInput(attrs={'size':'40'}))
	class Meta:
		model = CustomUser
	
		fields = ['username', 'email', 'first_name', 'last_name','date_of_birth', 'location', 'reason','password1', 'password2']
		#widgets={
			#'date_of_birth':DateInput(),
		#}

	
class TherapistSignupForm(UserCreationForm):
	username=forms.CharField(label='Enter a username',widget=forms.TextInput(attrs={'placeholder':'JonDoe','size':'40'}))
	email=forms.EmailField(label='Enter your email address',widget=forms.EmailInput(attrs={'placeholder': 'jondoe@example.com','size':'40'}))
	name=forms.CharField(label='Enter your name',widget=forms.TextInput(attrs={'placeholder':'Jon','size':'40'}))
	office_address=forms.CharField(label='Enter your office address',widget=forms.Textarea(attrs={'size':'45'}))
	qualification=forms.CharField(label='Enter your qualification',widget=forms.TextInput(attrs={'size':'40'}))
	specialization_area=forms.CharField(label="What is your area of specialization?",widget=forms.Textarea(attrs={'size':'45'}))
	password1=forms.CharField(label='Create a password',widget=forms.PasswordInput(attrs={'size':'40'}))
	password2=forms.CharField(label='Type your password again',widget=forms.PasswordInput(attrs={'size':'40'}))
	class Meta:
		model = CustomUser
	
		fields = ['username','email','name','office_address','qualification','specialization_area','password1','password2']