from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
app_name="therapist_dashboard"
urlpatterns = [
	path('profile/',views.ProfileView,name='profile'),
	
	path('questions/',views.QuestionView),
	path('questions/<int:pk>/your_answers/',views.AnswerView),
	path('questions/<int:pk>/answer/',views.NewAnswerView),
	path('questions/<int:pk>/your_answers/<int:pk_alt>/edit/',views.AnswerUpdateView),
	path('home/',views.HomeView,name="home"),
]
#path('patients/',views.PatientsView.as_view()),