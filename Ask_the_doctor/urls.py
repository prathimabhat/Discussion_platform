from django.conf.urls import url, include
from django.urls import path
from . import views
app_name="Ask_the_doctor"
urlpatterns=[
	path('',views.TherapistView.as_view()),
	
	path('ask/<int:pk>/',views.NewQuestionView.as_view(), name="ask"),
	path('my_questions/<int:pk>/',views.MyQuestions.as_view()),
	path('my_questions/<int:pk>/edit/',views.QuestionUpdateView),
	#path('search/',views.search_bar,name='search'),




]
