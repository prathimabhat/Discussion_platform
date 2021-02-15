from django.contrib.auth.decorators import login_required,user_passes_test



ther_login_required=user_passes_test(lambda u: False if u.is_normal_user else True)

def therapist_login_required(view_func):
	decorated_view_func = login_required(ther_login_required(view_func))
	return decorated_view_func
