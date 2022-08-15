from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib import messages

from hod.models import Hod
from students.models import Student
from helpers.credentials import dev_prod_email

dev_prod_email = dev_prod_email()

# THIS FUNCTION PREVENT USER 
# FROM ACCESSING CERTAIN URL IF AUTHENTICATED
def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name
			if group == 'students':
				return redirect('students:dashboard')
			else:
				return redirect('ecfr_admin:student/dashboard')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper_func
	return decorator

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'hod':
			return redirect('ecfr_admin:dashboard')

		if group == 'exam_n_record':
			return view_func(request, *args, **kwargs)

	return wrapper_function


def verify_email(view_func):
	def wrapper_funct(request, *args, **kwargs):
		if dev_prod_email == "local":
			return view_func(request, *args, **kwargs)
		else:
			user_status=None
			if request.user.groups.all()[0].name == 'students':
				u = Student.objects.filter(student=request.user.id).values('mat_no','active')
				user_type='students'
			else:
				u = Hod.objects.filter(hod=request.user.id).values('mat_no','active')
				user_type='other'

			for u in u:
				user_status = u['active']
				mat_no = u['mat_no'].replace('/','|')
			print('user_statusddddd '+str(user_status))
			# print(request._current_scheme_host + request.path)
			# print(request.get_host() + request.path)
			if user_status==0:
				if request.user.email:
					mail = send_mail(
					'Email Testing', # subject
					'Click here to verify your account > https://ecfr-rsu.herokuapp.com/verify/email/?mat='+str(mat_no)+'/&type='+str(user_type), # body
					'noreply@newworldjournals.com', # from
					[request.user.email], #['devarchive2020@gmail.com'],  to
					fail_silently = False,
					)
					if mail==1:
						# collect user url and redirect back to that url after some seconds
						print('Email sent')
						messages.success(request, 'Email sent, check your mailbox to verify your email.')
						return redirect(request.META.get('HTTP_REFERER'))
					else:
						print('Email not sent')
						print(mail)
						messages.success(request, 'Email not send, Please resend email')
						return redirect(request.META.get('HTTP_REFERER'))
				else:
					# collect user url and redirect back to that url after some seconds
					messages.success(request, 'Please update your account.')
					return redirect(request.META.get('HTTP_REFERER'))
			else:
				return view_func(request, *args, **kwargs)
	return wrapper_funct

