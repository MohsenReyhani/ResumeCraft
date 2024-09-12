
from django.contrib import messages
import re

class Tags:
	MOADI_NOT_FOUND = "moadi_not_found";

def remove_was_success(request):
	msg_status = messages.SUCCESS
	msg_content = "حذف با موفقیت انجام شد"
	messages.add_message(request, msg_status, msg_content)

def unkown_prosses_form(request, errors):
	msg_status = messages.ERROR
	msg_content = clean_errors(errors)
	print("unkown_prosses: ", errors, msg_content)
	if msg_content == "":
		msg_content = "خطا نامشخصی در ثبت فرم پیش آمده است"

	messages.add_message(request, msg_status, msg_content)

def create_edit_was_success(request, is_edit, name):
	msg_status = messages.SUCCESS
	if is_edit:
		msg_content = "تغییرات با موفقیت ثبت شد"
	else:
		msg_content = name +  " با موفقیت ثبت شد"
	messages.add_message(request, msg_status, msg_content)

def create_edit_question_was_success(request, is_edit, name):
	msg_status = messages.SUCCESS
	if is_edit:
		msg_content = "تغییرات با موفقیت ثبت شد. حداکثر تا 24 ساعت دیگر پرسش شما پاسخ داده خواهد شد."
	else:
		msg_content = name +  "با موفقیت ثبت شد. حداکثر تا 24 ساعت دیگر پرسش شما پاسخ داده خواهد شد."
	messages.add_message(request, msg_status, msg_content)

def moady_not_found(request):
	msg_status = messages.ERROR
	msg_content = "متاسفانه مودی یافت نشد، لطفا اول مودی ثبت فرمایید"
	messages.add_message(request, msg_status, msg_content, extra_tags=Tags.MOADI_NOT_FOUND)

def clean_errors(errors):
    result = ''
    for field, error_list in errors.items():
        for error in error_list:
            content = re.sub(r'<[^>]+>', '', str(error))
            if result == '':
                result += content
            else:
                result += '\n' + content
    return result

def errors(request, errors):
	msg_status = messages.ERROR
	msg_content = ""
	for error in errors:
		msg_content += error + "\n"
	if msg_content == "":
		msg_content = "خطا نامشخصی در ثبت فرم پیش آمده است"

	messages.add_message(request, msg_status, msg_content)

def error(request, error):
	msg_status = messages.ERROR
	if error == "":
		error = "خطا نامشخصی در ثبت فرم پیش آمده است"

	messages.add_message(request, msg_status, error)
