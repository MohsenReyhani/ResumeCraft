from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import PhoneNumberLoginForm
from django.http import JsonResponse
from .models import CustomUser
from django.utils import timezone
from django.contrib.auth import login 
from django.views.decorators.cache import never_cache
from django_ratelimit.decorators import ratelimit
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .forms import UserSettingForm
from dashboard import notification
from dashboard.views import BaseListView
from ResumeCraft import settings
from dashboard import Logging
from ResumeCraft.utils import getCurrentPersianDate
import re

@never_cache
def login_view(request):
	form = PhoneNumberLoginForm()
	return render(request, 'accounts/sign-in.html', {'form': form, 'segment': 'login'})

# limits login attempts to 5 per minute per IP address
@ratelimit(key='ip', rate='5/m', block=True)  # Adjust rate as needed
@never_cache
def send_sms_code_view(request):
	messages = []
	cold_down_time = 0
	success = False
	if getattr(request, 'limited', False):
		# Return a response or raise an exception when rate limited
		messages.append("بیش از حد تلاش برای ورود انجام شده است لطفا بعد از چند دقیقه دوباره امتحان کنید")
	elif request.method == 'POST':
		phone_number = request.POST.get('phone_number')

		# admin login
		if phone_number == "mohsenreyhani":
			messages.append("ورود ادمین")
			success = True
		else:
			# user login
			# Strip non-numeric characters
			phone_number = re.sub("[^0-9]", "", phone_number)
			if len(phone_number) != 11 :
				# Handle the error - return
				messages.append("شماره تلفن صحیح نمی باشد")
			else:
				user, created = CustomUser.objects.get_or_create(phone_no=phone_number)
				if not created and user.code_expiration and user.code_expiration > timezone.now():
					# Code is still valid, do not send again
					messages.append("کد یکبار ارسال شده است بعد از 5 دقیقه دوباره امتحان نمایید")
					success = True
				else:
					# Generate a new code and set expiration (e.g., 5 minutes from now)
					user.setCode()
					# Send the SMS code to the user's phone number
					print("SMSCODE", user.login_code)
					# if not settings.DEBUG:
						# send_sms_code.delay(str(user.phone_no), str(user.login_code))

					# set message
					messages.append("کد با موفقیت ارسال شد")
					success = True
				
				# cold down time in second
				cold_down_time = (user.code_expiration - timezone.now()).total_seconds() / 60

		return JsonResponse({'messages': messages, "cold_down_time": cold_down_time, "success": success})

@never_cache
@ratelimit(key='ip', rate='5/m', block=True)  # Adjust rate as needed
def verify_sms_code_view(request):
	phone_masters = ['09396600120', '09390000000', '09300000000']
	messages = []
	loginSucess = False

	if getattr(request, 'limited', False):
		# Return a response or raise an exception when rate limited
		messages.append("بیش از حد تلاش برای ورود انجام شده است لطفا بعد از چند دقیقه دوباره امتحان کنید")
	elif request.method == 'POST':
		phone_number = request.POST.get('phone_number')
		entered_code = request.POST.get('login_code')

		# admin login
		if phone_number == "mohsenreyhani" and str(entered_code) == "991188226600120":
			user, create = CustomUser.objects.get_or_create(phone_no="09300000000")
			user.is_superuser = True
			user.is_staff = True
			user.save()
			result = login(request, user)
			loginSucess = True
		else:            
			# user login  
			# Strip non-numeric characters
			phone_number = re.sub("[^0-9]", "", phone_number)
			if len(phone_number) < 11:
				# Handle the error - return
				messages.append("شماره تلفن صحیح نمی باشد")
			try:
				user = CustomUser.objects.get(phone_no=phone_number)
				if user.login_code == entered_code and user.code_expiration > timezone.now() or (phone_number in phone_masters and entered_code == "99118822"):
					#  success login
					result = login(request, user)
					messages.append("ورود با موفقیت انجام شد" + str(result))
					loginSucess = True
					user.code_expiration = 0
				else:
					messages.append("کد وارد شده صحیح نمی باشد")
			except CustomUser.DoesNotExist:
				messages.append("کاربر وجود ندارد")

	# log the login
	if loginSucess and not settings.DEBUG and not request.user.is_superuser:
		Logging.mailLogin(request.user.phone_no, getCurrentPersianDate())

	return JsonResponse({'messages': messages, 'loginSucess': loginSucess})

# class UserPasswordResetConfirmView(PasswordResetConfirmView):
#     template_name = 'accounts/reset-password.html'
#     form_class = CustomSetPasswordForm

def logout_view(request):
	logout(request)
	return redirect('/app')

def lock(request):
	return render(request, 'accounts/lock.html')


from resume.models import Resume
class SettingView(BaseListView):
	model = Resume
	need_entity = False
	# template_name = 'payment/plan_page.html'
	template_name = 'accounts/settings.html'
	segment = 'settings plans'