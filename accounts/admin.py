from django.contrib import admin
from django.db import models
from .models import CustomUser
from dashboard.models import UserPreferences
from ResumeCraft.utils import convertToFaDate

class CustomuserAdmin(admin.ModelAdmin):

    ordering = ['-created_at']
    
    list_display = ('phone_no', 'first_name', 'last_name', 'fa_date_joined',
                     'is_active', 'is_staff', 'login_code', 'fa_code_expiration', 'credit_value', 'credit_expire_at')
    
    def credit_value(self, obj):
        userPref, created = UserPreferences.objects.get_or_create(user=obj)
        return userPref.credit

    def credit_expire_at(self, obj):
        userPref, created = UserPreferences.objects.get_or_create(user=obj)
        return str(userPref.credit_in_days()) + " روز"
    
    def fa_date_joined(self, obj):
        return convertToFaDate(obj.date_joined)
    
    def fa_code_expiration(self, obj):
        if obj.code_expiration != None:
            return convertToFaDate(obj.code_expiration)
        else:
            None
   
admin.site.register(CustomUser, CustomuserAdmin)

