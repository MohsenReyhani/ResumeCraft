from django.core.mail import send_mail

def mailLogin(phonenumber, currentDate):
	try:
		send_mail(
			'Ezfactor Notification Login',
			str(phonenumber) + ' just logged in ' + str(currentDate),
			'info@ezfactor.ir', # From email
			['mohsenreyhani@gmail.com'], # To email
			fail_silently=False,
		)
	except Exception as e:
		print("Error in Sending Loggin Email: ",e)

def mailPurchased(refrenceId, status, order, phone_no):
	try:
		send_mail(
			str(phone_no) + ' just purchased ',
			'info@ezfactor.ir', # From email
			['mohsenreyhani@gmail.com'], # To email
			fail_silently=False,
		)
	except Exception as e:
		print("Error in Sending Purchased Email: ",e)
