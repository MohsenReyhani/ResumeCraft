import datetime, time, jdatetime
from django.utils import timezone
from datetime import datetime as dt, timedelta
import pytz, json

# Convert the timestamp to milliseconds
def convertDate(dt):
	if dt:
		# Ensure the datetime is in UTC
		dt_utc = dt.astimezone(timezone.utc)
		unix_timestamp = dt_utc.replace(tzinfo=timezone.utc).timestamp()
		return int(unix_timestamp * 1000)
	else:
		return 0

def convertDateFromMillisecond(millisecond):
	dt = datetime.datetime.fromtimestamp(millisecond / 1000.0)
	jalali_date = jdatetime.date.fromgregorian(day=dt.day, month=dt.month, year=dt.year)
	time_str = dt.strftime("%H:%M:%S")
	jalali_datetime_str = str(jalali_date) + " " + str(time_str)
	return jalali_datetime_str

def combineDateAndCurrentTime(jalali_date):
	if jalali_date is None:
		return None
	
	current_time = timezone.localtime().time()
	combined_datetime = datetime.datetime.combine(jalali_date, current_time)
	combined_datetime = timezone.make_aware(combined_datetime, timezone.get_current_timezone())

	return combined_datetime

def getCurrentPersianDate():
	# Define a mapping of month numbers to Persian month names
	persian_months = {
		1: 'فروردین',
		2: 'اردیبهشت',
		3: 'خرداد',
		4: 'تیر',
		5: 'مرداد',
		6: 'شهریور',
		7: 'مهر',
		8: 'آبان',
		9: 'آذر',
		10: 'دی',
		11: 'بهمن',
		12: 'اسفند',
	}
	# Get the current datetime
	current_datetime = datetime.datetime.now()
	# Convert the current datetime to Jalali
	jalali_datetime = jdatetime.datetime.fromgregorian(datetime=current_datetime)
	# Extract the Persian month name
	persian_month_name = persian_months[jalali_datetime.month]
	# Format the Jalali datetime, inserting the Persian month name
	formatted_jalali_datetime = jalali_datetime.strftime('%Y ' + persian_month_name + ' %d _ %H:%M:%S')
	return formatted_jalali_datetime

def convertToFaDate(date, tz_name='Asia/Tehran'):
	if date.tzinfo is None:
		local_tz = pytz.timezone(tz_name)
		date = local_tz.localize(date)
	date = date.astimezone(pytz.timezone(tz_name))
	jalali_date = jdatetime.datetime.fromgregorian(datetime=date)
	return jalali_date.strftime('%Y/%m/%d %H:%M')

def getFaMonthName(monthNumber):
	# Get the month's name in Persian
	jalali_months = [
		"فروردین", "اردیبهشت", "خرداد", 
		"تیر", "مرداد", "شهریور", 
		"مهر", "آبان", "آذر", 
		"دی", "بهمن", "اسفند"
	]
	current_month_name = jalali_months[monthNumber-1]
	return current_month_name

def convertFaDateToGorgian(jalali_date_str, customFromat="%Y.%m.%d"):
	jalali_date = jdatetime.datetime.strptime(jalali_date_str, customFromat)
	gregorian_date = jalali_date.togregorian()
	local_tz = pytz.timezone('Asia/Tehran')
	aware_gregorian_date = local_tz.localize(dt(gregorian_date.year, gregorian_date.month, gregorian_date.day))
	return aware_gregorian_date.isoformat()

def convertFaDateToGorgianForms(jalali_date_str):
	jalali_date = jdatetime.datetime.strptime(jalali_date_str, "%Y.%m.%d")
	gregorian_date = jalali_date.togregorian()
	converted_date = dt(gregorian_date.year, gregorian_date.month, gregorian_date.day).date()
	return converted_date

def correct21DaysTimeSet(jalai_date):
	current_date = dt.now().date()
	# Check if the date is before 21 days from now
	adjusted_date = current_date - timedelta(days=21)
	if jalai_date < adjusted_date:
		return adjusted_date
	else:
		return jalai_date

class DateEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, datetime.date):
			return obj.isoformat()
		return json.JSONEncoder.default(self, obj)
	

