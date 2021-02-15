from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    
	path("home/", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    
   	path('reset_password/',
	auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html",email_template_name = 'accounts/password_reset_email.html'),
	name="password_reset"),

    path('reset_password_sent/', 
    auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
    name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
    name="password_reset_confirm"),

    path('reset_password_complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
    name="password_reset_complete"),

    path('therapist_signup/',views.therapist_signup,name="therapist_signup")

]