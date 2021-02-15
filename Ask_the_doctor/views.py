from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from accounts.models import Therapist
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import QuestionForm,QuestionUpdateForm
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView,CreateView
from .models import question_to_therapist,answers_from_therapist
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
#from .forms import PatientForm
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template

from community_forum.models import Questions

'''
@login_required
def PatientRegistrationView(request,*args,**kwargs):
	form=PatientForm
	if request.method=='POST':
		form=PatientForm(request.POST)
		if form.is_valid():
			user_=get_object_or_404(Profile,id=request.user.profile.id)
			therapist_= get_object_or_404(Therapist, pk=kwargs['pk'])
			patient=form.save(commit=False)
			patient.user=user_
			patient.therapist=therapist_
			patient.save()
			form.save_m2m()
			return redirect("Ask_the_doctor:ask",id=therapist_.id)
		else:
			form=PatientForm()
	else:
		form=PatientForm()

	context={
	'form':form
	}
    
	return render(request,'Ask_the_doctor/patientform.html',context)
'''
class TherapistView(LoginRequiredMixin,View):

	def get(self, request, *args, **kwargs):

		therapists=Therapist.objects.all()
		context={
			'therapists':therapists
		}
		return render(request,'Ask_the_doctor/ask_the_doctor.html',context)



class NewQuestionView(LoginRequiredMixin,CreateView):
	
	model=question_to_therapist
	form_class=QuestionForm
	#success_url='NewQuestionView'
	
	def get_queryset(self):
		self.therapist = get_object_or_404(Therapist, pk=self.kwargs['pk'])
		return Therapist.objects.filter(pk=self.therapist)

	
	def form_valid(self,form):
		therapist_= get_object_or_404(Therapist, pk=self.kwargs['pk'])
		obj=form.save(commit=False)
		obj.user=self.request.user.profile
		obj.therapist=therapist_
		obj.save()
		subject='New message'
		from_email=settings.EMAIL_HOST_USER
		to_email=therapist_.therapist_email
		text_content="Hi, you have a new message!"
		html_content=get_template("private_chats/msg_received_email.html").render()
		msg= EmailMultiAlternatives(subject,text_content,from_email,[to_email])
		msg.attach_alternative(html_content, "text/html")
		msg.send()

		#return self.render_to_response(self.form_valid(form))
		return self.render_to_response(self.get_context_data(form=form))
		#return super().form_valid(form)


	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		user_=self.request.user.profile
		context["questions"] = question_to_therapist.objects.filter(user=user_).order_by('id')

		return context

	'''def get(self,request,*args,**kwargs):
		return render(request,'ask_the_doctor/ask.html')

	def post(self,request,*args,**kwargs):

		questionform = QuestionForm(request.POST)
		
		therapist_ = get_object_or_404(Therapist, pk=self.kwargs.get('pk'))
		if questionform.is_valid():
			question = questionform.save(commit=False)
			question.user = request.user.profile
			question.therapist=therapist_
			
			question.question=questionform.cleaned_data.get('question')

			question.save()
			return render(request,'ask_the_doctor/ask.html',{'form' :questionform})
			#return render('ask_the_doctor/ask/<int:pk>/')

		return render(request,'ask_the_doctor/')
	'''

class MyQuestions(LoginRequiredMixin,View):

	def get(self,request,*args,**kwargs):
		question_id=kwargs['pk']
		question=question_to_therapist.objects.filter(id=question_id)
		answers=answers_from_therapist.objects.filter(question=question_id)
		context={
			'question':question,
			'answers':answers
		}
		return render(request,'Ask_the_doctor/my_questions.html',context)



@login_required
def QuestionUpdateView(request,*args,**kwargs):
	context={}
	question_id=kwargs['pk']
	#answer_id=kwargs['pk_alt']
	obj=get_object_or_404(question_to_therapist,id=question_id)
	form=QuestionUpdateForm(request.POST or None,instance=obj)
	if form.is_valid():
		form.save()
		#redirect_url=reverse('therapibvst_dashboard:AnswerView',args=[question_id])
		return redirect('/ask_the_doctor/')
	context["form"]=form
	return render(request,'Ask_the_doctor/question_update.html',context)

'''
@login_required
def search_bar(request,*args,**kwargs):
	
    if request.method=='GET':
           
        search_query = request.GET.get('to', None)
        if search_query:
            question_list = Questions.objects.filter(title__icontains=search_query)

   
            context={   
            
            'question_list':question_list
           
            }
        
    return render(request, "Ask_the_doctor/base.html",context)
'''