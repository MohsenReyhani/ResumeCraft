from django import template
from dashboard.models import UserPreferences

register = template.Library()

@register.filter(name='get_credit_is_valid')
def get_credit_is_valid(user):
	userPref, created = UserPreferences.objects.get_or_create(user=user)
	return userPref.credit_is_valid()

@register.filter(name='get_credit_days')
def get_credit_days(user):
	userPref, created = UserPreferences.objects.get_or_create(user=user)
	return userPref.credit_in_days()

@register.filter(name='get_credit_value')
def get_credit_value(user):
	userPref, created = UserPreferences.objects.get_or_create(user=user)
	return userPref.credit

@register.filter(name='get_credit_expire_at')
def get_credit_expire_at(user):
	userPref, created = UserPreferences.objects.get_or_create(user=user)
	return userPref.credit_expire_at



