from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
app_name="user_profile"
urlpatterns = [
	path('',views.ProfileView.as_view()),
	path('my_questions/',views.MyQuestionsView.as_view()),
	path('my_answers/',views.MyAnswersView.as_view()),
	path('my_questions/<int:pk>/edit/',views.QuestionUpdateView),
	path('my_answers/<int:pk>/edit/',views.AnswerUpdateView),
	path('my_questions/<int:pk>/delete/',views.QuestionDeleteView),
	path('my_answers/<int:pk>/delete/',views.AnswerDeleteView)

]