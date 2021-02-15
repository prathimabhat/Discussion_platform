from django.shortcuts import render,redirect
#from accounts.mixins import GroupRequiredMixin
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404,HttpResponseRedirect
from accounts.models import Therapist
#from .models import Patients
from Ask_the_doctor.models import question_to_therapist,answers_from_therapist
from django.views.generic import CreateView
from .forms import AnswerForm,AnswerUpdateForm
from accounts.decorators import therapist_login_required
#class DemoView(GroupRequiredMixin, View):
  #group_required = [u'therapists']
@therapist_login_required
def ProfileView(request, *args, **kwargs):
	

	user_=request.user
	user=get_object_or_404(Therapist,user=user_)
	context={
	    'user':user
	}
	return render(request,'therapist_dashboard/profile.html',context)

'''class PatientsView(LoginRequiredMixin,View):
	def get(self,request,*args,**kwargs):
		patients=Patients.objects.filter(therapist=self.request.user.therapist)
		context={
			'patients':patients
		}
		return render(request,'therapist_dashboard/patients.html',context)
'''
@therapist_login_required
def QuestionView(request,*args,**kwargs):


	question=question_to_therapist.objects.filter(therapist=request.user.therapist).order_by('-date')

	context={
		'question':question,
		
	}
	return render(request,'therapist_dashboard/questions.html',context)

@therapist_login_required
def AnswerView(request,*args,**kwargs):

	
	question_id=kwargs['pk']
	question=get_object_or_404(question_to_therapist,id=question_id)
	answers=answers_from_therapist.objects.filter(question=question_id).order_by('-date')

	context={
		'question':question,
		'answers':answers,
		
	}
	return render(request,'therapist_dashboard/answers.html',context)

'''class NewAnswerView(CreateView,LoginRequiredMixin):

	model=answers_from_therapist
	form_class=AnswerForm
	success_url='/therapist_dashboard/questions/'
	
	def form_valid(self,form):
		
		question_=get_object_or_404(question_to_therapist,id=self.kwargs['pk'])
		obj=form.save(commit=False)
		obj.therapist=self.request.user.therapist
		obj.user=question_.user
		obj.question=question_.id
		obj.save()
		return super().form_valid(form)
'''
@therapist_login_required

def NewAnswerView(request,*args,**kwargs):
	form=AnswerForm
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		if form.is_valid():

			answer = form.save(commit=False)
			question_=get_object_or_404(question_to_therapist,id=kwargs['pk'])

			answer.therapist=request.user.therapist
			answer.user=question_.user
			answer.question=question_

			answer.save()
			return redirect('/therapist_dashboard/questions/')
		else:
			form = AnswerForm()
	return render(request, 'therapist_dashboard/answers_from_therapist_form.html', {'form': form})


@therapist_login_required
def AnswerUpdateView(request,*args,**kwargs):
	context={}
	question_id=kwargs['pk']
	answer_id=kwargs['pk_alt']
	obj=get_object_or_404(answers_from_therapist,id=answer_id)
	form=AnswerUpdateForm(request.POST or None,instance=obj)
	if form.is_valid():
		form.save()
		#redirect_url=reverse('therapist_dashboard:AnswerView',args=[question_id])
		return redirect('/therapist_dashboard/questions/')
	context["form"]=form
	return render(request,'therapist_dashboard/answer_update.html',context)
@therapist_login_required
def HomeView(request,*args,**kwargs):
	return render(request,'therapist_dashboard/home.html')