from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from accounts.models import CustomUser
from django.db.models import JSONField
from django.utils import timezone
from datetime import datetime, timedelta

class UserPreferences(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	sorting_preferences = JSONField(default=dict)
	credit = models.IntegerField(default = 0)
	credit_expire_at = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f"{self.user.phone_no}'s sorting preferences"
	
	def getKeySort(self, appname, key):
		return self.sorting_preferences.get(appname).get(key)
	
	def getNextOrder(self, appname, key):
		sort_order = self.sorting_preferences.get(appname).get(key)
		if sort_order == "asc" :
			return "desc"
		elif sort_order == "desc":
			return  ""
		else:
			return "asc"
		
	# Credit	
	def credit_in_days(self):
		remaninigTime = self.credit_expire_at - timezone.now()
		return int(remaninigTime.days)

	def credit_is_valid(self):
		if self.credit > 0 and self.credit_expire_at > timezone.now():
			return True
		return False

	def use_credit(self):
		if self.credit_is_valid():
			self.credit -= 1
			self.save()
			return True
		return False

	def charge_credit(self, value, period_in_days):
		self.credit = value
		self.credit_expire_at = timezone.now() + timedelta(days=period_in_days)
		self.save()