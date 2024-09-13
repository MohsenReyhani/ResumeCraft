from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ResumeCraft import settings as appsetting
from django.http import JsonResponse
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.core.cache import cache
from persiantools.jdatetime import JalaliDate
from django.views.generic.edit import FormView
import json
from django.db.models import Q
from functools import reduce
from accounts.models import CustomUser
from .models import UserPreferences

# Index
def index(request):
	return render(request, 'pages/index.html')

# Dashboard
@never_cache
@login_required(login_url="accounts/login/")
def dashboard(request):

	showFillNamePopUp = False

	# show popup for name first
	if request.user.first_name == None and request.user.last_name == None:
		showFillNamePopUp = True
	
	context = {
		'segment': 'dashboard',
		'showFillNamePopUp': showFillNamePopUp
	}
	return render(request, 'dashboard/dashboard.html', context)

# @login_required(login_url="app/accounts/login/")
# def settings(request):
# 	context = {
# 		'segment': 'settings'
# 	}
# 	return render(request, 'pages/settings.html', context)

def colorPalette(request):
	colorBlack = {'name': 'black', 'color': '#2C3E50', 'r': '44', 'g': '62', 'b': '80'}
	colorWhite = {'name': 'white', 'color': '#ECF0F1', 'r': '236', 'g': '240', 'b': '241'}
	colorAlert = {'name': 'red', 'color': '#FF4500', 'r': '255', 'g': '69', 'b': '0'}
	colorAccent = {'name': 'orange', 'color': '#F39C12', 'r': '243', 'g': '156', 'b': '18'}
	colorSecond = {'name': 'blue green', 'color': '#1ABC9C', 'r': '26', 'g': '188', 'b': '156'}
	colorPrimary = {'name': 'dark green', 'color': '#16A085', 'r': '22', 'g': '160', 'b': '133'}
	items = [colorBlack, colorWhite, colorAlert, colorAccent, colorSecond, colorPrimary]
	
	context = {
		'segment': 'color_palette',
		'items': items
	}
	return render(request, 'dashboard/color_palette.html', context)

@never_cache
@login_required(login_url="/app/accounts/login/")
def fillNames(request):
	if request.method == 'POST':
	
		first_name = request.POST.get('first_name', '')
		last_name = request.POST.get('last_name', '')

		user = CustomUser.objects.get(phone_no=request.user.phone_no)
		user.first_name = first_name
		user.last_name = last_name
		user.save()

		return JsonResponse({'success': True})
	
@never_cache
def tutorials(request):	
	context = {
		'segment': 'tutorials',
	}
	return render(request, 'dashboard/tutorials.html', context)

# # Tables
# @login_required(login_url="/app/accounts/login/")
# def bs_tables(request):
# 	context = {
# 		'parent': 'tables',
# 		'segment': 'bs_tables',
# 	}
# 	return render(request, 'pages/tables/bootstrap-tables.html', context)

# # Components
# @login_required(login_url="/app/accounts/login/")
# def buttons(request):
# 	context = {
# 		'parent': 'components',
# 		'segment': 'buttons',
# 	}
# 	return render(request, 'pages/components/buttons.html', context)

# @login_required(login_url="/app/accounts/login/")
# def notifications(request):
# 	context = {
# 		'parent': 'components',
# 		'segment': 'notifications',
# 	}
# 	return render(request, 'pages/components/notifications.html', context)

# @login_required(login_url="/app/accounts/login/")
# def forms(request):
# 	context = {
# 		'parent': 'components',
# 		'segment': 'forms',
# 	}
# 	return render(request, 'pages/components/forms.html', context)

# @login_required(login_url="/app/accounts/login/")
# def modals(request):
# 	context = {
# 		'parent': 'components',
# 		'segment': 'modals',
# 	}
# 	return render(request, 'pages/components/modals.html', context)

# @login_required(login_url="/app/accounts/login/")
# def typography(request):
# 	context = {
# 		'parent': 'components',
# 		'segment': 'typography',
# 	}
# 	return render(request, 'pages/components/typography.html', context)

# Errors
@never_cache
def error_404(request):
	return render(request, 'pages/examples/404.html')

@never_cache
def error_500(request):
	return render(request, 'pages/examples/500.html')

# Extra
def upgrade_to_pro(request):
	return render(request, 'pages/upgrade-to-pro.html')

class BaseListView(TemplateView):
		# model for query
		model = None
		# template to show in view
		template_name = ''
		# page name
		segment = ''
		# search column names for searching query
		search_fields = []
		# cache for performance speed
		use_cache = False
		base_cache_key = ""
		cache_key = ""
		# no created_by (for stuff)
		created_by_disable = False

		default_sort = "-created_at"

		def dispatch(self, request, *args, **kwargs):
			dispatch_func = super().dispatch
			dispatch_func = never_cache(dispatch_func)
			dispatch_func = login_required(dispatch_func)
			return dispatch_func(request, *args, **kwargs)
		
		def edit_data_list(self, datalist):
			return datalist
		
		def date_query(self):
			query = Q()

			fromDate = self.request.GET.get('from_date', '')
			toDate = self.request.GET.get('to_date', '')
			# Convert to Gregorian dates
		
			# Add filters based on the presence of start_date and end_date
			if fromDate != "":
				from_jalali = JalaliDate(*map(int, fromDate.split('-')))
				from_gregorian = from_jalali.to_gregorian()
				query.add(Q(creation_date__date__gte = from_gregorian), Q.AND)
			if toDate != "":
				to_jalali = JalaliDate(*map(int, toDate.split('-')))
				to_gregorian = to_jalali.to_gregorian()
				query.add(Q(creation_date__date__lte = to_gregorian), Q.AND)

			return query
		

		def get_data_list(self, search_content=""):

			if self.created_by_disable:
				query = Q()
			else:
				query = Q(created_by = self.request.user)

			search_query = Q()
			if search_content.strip() != "":
				for field in self.search_fields:
					key = '{}__icontains'.format(field)
					# filters[key] = search_content
					# query.add(Q(key=search_content), Q.OR)
					search_query.add(Q(**{"%s__icontains" % field: search_content}), Q.OR)

			query.add(search_query, Q.AND)
			query.add(self.date_query(), Q.AND)

			sortbyList = []
			preferences, created = UserPreferences.objects.get_or_create(user=self.request.user)
			current_prefs = preferences.sorting_preferences

			if self.segment in current_prefs:
				sortPreferences = current_prefs[self.segment]
				for key, value in sortPreferences.items():
					if value == "asc":
						sortbyList.append(key)
					elif value == "desc":
						sortbyList.append("-"+key)
			
			if self.created_by_disable:
				return self.model.objects.filter(query)
			else:
				if len(sortbyList) == 0:
					sortbyList.append(self.default_sort)
				return self.model.objects.filter(query).order_by(*sortbyList)

		def get_context_data(self, **kwargs):
			context = super().get_context_data(**kwargs)

			page_number = self.request.GET.get('page', 1)
			# search content
			search_content = self.request.GET.get('search', "")
			# sort based on columns
			# sort_field = self.request.GET.get('sort_field', '-created_by')
			# sort_order = self.request.GET.get('sort_order', 'asc')
			# sort_by = f'-{sort_field}' if sort_order == 'desc' else sort_field

			if self.use_cache:
				self.cache_key = self.base_cache_key + search_content
				data_list = cache.get(self.cache_key)
		
			context['segment'] = self.segment

			keyList, valueList = self.add_values()
			for key, value in zip(keyList, valueList):
				context[key] = value

			# data_list = self.get_data_list(search_content, sort_by)
			data_list = self.get_data_list(search_content)
			data_list = self.edit_data_list(data_list)
			if self.use_cache:
				cache.set(self.cache_key, data_list, 3600) 
			
			LIST_SIZE = 20
			paginator = Paginator(data_list, LIST_SIZE)
			context['page'] = paginator.get_page(page_number)

			return context
		
		def add_values(self):
			return [], []
		
		def post(self, request, *args, **kwargs):
			return self.handle_post(request, *args, **kwargs)

		def handle_post(self, request, *args, **kwargs):
			return render(request, self.template_name)

@never_cache
@login_required(login_url="/app/accounts/login/")
def update_sorting_preferences(request):
	if request.method == 'POST':

		# Split the request path
		app_name = request.POST.get('app_name')
		field_name = request.POST.get('field_name')

		preferences, created = UserPreferences.objects.get_or_create(user=request.user)
		current_prefs = preferences.sorting_preferences

		if app_name not in current_prefs:
			current_prefs[app_name] = {}

		sort_order = preferences.getNextOrder(app_name, field_name)
		if sort_order == "":
			current_prefs[app_name].pop(field_name, None)
		else:
			current_prefs[app_name][field_name] = sort_order

		preferences.sorting_preferences = current_prefs
		preferences.save()

		return JsonResponse({'status': 'success'})
	
	return JsonResponse({'status': 'error'}, status=400)

@never_cache
@login_required(login_url="/app/accounts/login/")
def get_sorting_preferences(request):
	if request.method == 'GET':

		# Split the request path
		app_name = request.GET.get('app_name')
		preferences, created = UserPreferences.objects.get_or_create(user=request.user)
		sorting_prefs = preferences.sorting_preferences.get(app_name, {})
		return JsonResponse({'status': 'success', 'result': sorting_prefs})
		