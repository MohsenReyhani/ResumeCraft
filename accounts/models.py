from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import Permission, Group  # Import Permission and Group
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
import random
# comment this line for first migration

class CustomUserManager(BaseUserManager):
	def create_user(self, phone_no, password=None, **extra_fields):
		if not phone_no:
			raise ValueError('The Phone No field must be set')
		# email = self.normalize_email(email)
		user = self.model(phone_no=phone_no, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, phone_no, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self.create_user(phone_no, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(blank=True, null=True)
	first_name = models.CharField(max_length=30, blank=True, null=True)
	last_name = models.CharField(max_length=30, blank=True, null=True)
	phone_no = models.CharField(unique=True, max_length=13, blank=True, null=True)
	date_joined = models.DateTimeField(default=timezone.now)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	# comment this line for first migration
	login_code = models.CharField(max_length=6, blank=True, null=True)
	code_expiration = models.DateTimeField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

	objects = CustomUserManager()

	USERNAME_FIELD = 'phone_no'
	REQUIRED_FIELDS = []

	def __str__(self):
		return str(self.phone_no)
	
	class Meta:
		# Add a related_name for the groups field
		permissions = [
			("custom_permission", "Custom Permission"),
		]

	# Specify custom related_names for the groups and user_permissions fields
	groups = models.ManyToManyField(
		Group,
		verbose_name= 'groups',
		blank=True,
		related_name='custom_users',  # Specify a custom related_name
		help_text=
			'The groups this user belongs to. A user will get all permissions granted to each of their groups.'
	)
	
	user_permissions = models.ManyToManyField(
		Permission,
		verbose_name= 'user permissions',
		blank=True,
		related_name='custom_users_permissions',  # Specify a custom related_name
		help_text= 'Specific permissions for this user.',
	)

	# 5 minutes login code expireation time
	def setCode(self):
		self.login_code = str(random.randint(100000, 999999))
		self.code_expiration = timezone.now() + timezone.timedelta(minutes=5)
		self.save()

	def getfullname(self):
		fisrtName = "" if self.first_name is None else self.first_name
		lastName = "" if self.last_name is None else self.last_name
		return str(fisrtName) + " " + str(lastName)
	