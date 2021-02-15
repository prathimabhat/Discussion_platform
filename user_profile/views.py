from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from community_forum.models import Questions,Answers
from .forms import QuestionUpdateForm,AnswerUpdateForm

class ProfileView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):

        user_=self.request.user
        user=get_object_or_404(Profile,user=user_)
        context={
            'user':user
        }
        return render(request,'user_profile/profile.html',context)

class MyQuestionsView(LoginRequiredMixin,View):
	def get(self,request,*args,**kwargs):
		questions=Questions.objects.filter(user=self.request.user.profile)
		context={
			'questions':questions
		}
		return render(request,'user_profile/questions.html',context)

class MyAnswersView(LoginRequiredMixin,View):
	def get(self,request,*args,**kwargs):

		answers=Answers.objects.filter(user=self.request.user.profile)
		#questions=Questions.objects.filter(id=question_id)
		context={
			'answers':answers
		}
		return render(request,'user_profile/answers.html',context)


@login_required
def QuestionUpdateView(request,*args,**kwargs):
	context={}
	question_id=kwargs['pk']
	obj=get_object_or_404(Questions,id=question_id)
	form=QuestionUpdateForm(request.POST or None,instance=obj)
	if form.is_valid():
		form.save()
		#redirect_url=reverse('therapist_dashboard:AnswerView',args=[question_id])
		return redirect('/profile/my_questions/')
	context["form"]=form
	return render(request,'user_profile/question_update.html',context)

@login_required
def AnswerUpdateView(request,*args,**kwargs):
	context={}
	answer_id=kwargs['pk']
	obj=get_object_or_404(Answers,id=answer_id)
	form=AnswerUpdateForm(request.POST or None,instance=obj)
	if form.is_valid():
		form.save()
		#redirect_url=reverse('therapist_dashboard:AnswerView',args=[question_id])
		return redirect('/profile/my_answers/')
	context["form"]=form
	return render(request,'user_profile/answer_update.html',context)

@login_required
def QuestionDeleteView(request,pk):
	obj=get_object_or_404(Questions,id=pk)
	if request.method=='POST':
		obj.delete()
		return redirect('/profile/my_questions/')
	return render(request,'user_profile/delete_question.html')

def AnswerDeleteView(request,pk):
	obj=get_object_or_404(Answers,id=pk)
	if request.method=='POST':
		obj.delete()
		return redirect('/profile/my_answers/')
	return render(request,'user_profile/delete_answer.html')