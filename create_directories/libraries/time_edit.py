import datetime
import re
import time
from datetime import date
from datetime import timedelta
import threading
from array import array

HALF_DAY_LENGTH_HOURS = 12
AM_PM:array = ["取得できていない．", "午前", "午後"]

def if_equal_time(time_a:datetime, time_b:datetime) -> bool:
	if(time_a.hour == time_b.hour):
		if(time_a.minute == time_b.minute):
			return True
		else:
			return False

def check_and_convert_AM_PM(str_input:str) -> int:
	if (str_input == "午前"):
		return 1
	elif (str_input == "午後"):
		return 2
	else:
		return 0

def input_AM_PM() -> function:
	AM_PM_input_str:str = input("午前/午後: ")
	AM_PM_input_int:int = check_and_convert_AM_PM(AM_PM_input_str)
	if (check_and_convert_AM_PM(AM_PM_input_str) != 0):
		return AM_PM_input_int
	else:
		print("入力が正しくないようです。")
		return input_AM_PM()

def hour_converter_from_AM_PM_to_24_foundation(hour_AM_PM:int, AM_or_PM_identifier:int) -> int:
	if (AM_or_PM_identifier == 0):
		hour_24_foundation = hour_AM_PM
	else:
		hour_24_foundation = hour_AM_PM + (HALF_DAY_LENGTH_HOURS * (AM_or_PM_identifier - 1))
	return hour_24_foundation

def create_time_info() -> dict:			
	print("好みの時間を入力してください。それが、現在時刻に等しいかどうか確認することができます。")
	AM_PM_input = input_AM_PM() # 午前か午後かの入力。
	hour_input = (int)(input("時間？: "))
	minute_input = (int)(input("何分？: "))
	time_dict = {'AM_or_PM_identifier': AM_PM_input, 'hour': hour_input, 'minute': minute_input }
	return time_dict

def create_datetime_with_AM_PM_time_dict_and_given_date(time_dict:dict, given_date:date) -> datetime:
	hour_24_foundation = hour_converter_from_AM_PM_to_24_foundation(time_dict['hour'], time_dict['AM_or_PM_identifier'])
	given_year = (int)(given_date.year)
	given_month = (int)(given_date.month)
	given_day = (int)(given_date.day)
	given_time = datetime.datetime(given_year, given_month, given_day, hour_24_foundation, time_dict['minute'])
	return given_time

def input_time_today() -> datetime:
	print("好みの時間を入力してください。")
	AM_PM_time_dict = create_time_info()
	current_date = date.today()
	given_datetime = create_datetime_with_AM_PM_time_dict_and_given_date(AM_PM_time_dict, current_date)
	print(given_datetime)
	return given_datetime

def get_current_time(current_t:datetime) -> None:
	today = current_t.strftime('%m月%d日%I:%M')
	another_today = current_t.strftime('%I:%M %m月%d日')
	print(today)
	# notify_time(current_t)

def get_current_24_foundation_time(current_t:datetime) -> None:
	print((str)(current_t.month) + "月" + (str)(current_t.day) + "日" + (str)(current_t.hour) + ":" + (str)(current_t.minute))
	# notify_24_foundation(current_t)

def get_current_24_foundation_hour(current_t:datetime) -> None:
	print(current_t.hour)
	# notify_hour(current_t)

def get_current_day(current_t:datetime) -> None:
	current_day = current_t.strftime('%A')
	print("CURRENT DAY: " + current_day)

def get_current_hour(current_t:datetime) -> None:
	current_hour = current_t.strftime('%I時')
	print("CURRENT HOUR: " + current_hour)
	# notify_hour(current_t)

def get_current_rough_minute(current_t:datetime) -> None:
	current_time = current_t.strftime('%M分')
	matched_object = re.search("^[0-9]", current_time, flags=0)
	print("CURRENT APPROXIMATE MINUTE: " + matched_object.group(0) + "0" + "~" + matched_object.group(0) + "9")

def get_current_minute(current_t:datetime) -> None:
	current_minute = current_t.strftime('%M分')
	print("CURRENT MINUTE: " + current_minute)

def get_current_hello_world(given_t:datetime) -> None:
	"""
	特定の時間になると、時間を表示する関数。
	"""
	while True:
		current_t = datetime.datetime.now()
		if (if_equal_time(current_t, given_t)):
			today = current_t.strftime('%m月%d日%I:%M')
			print("CURRENT_TIME: " + today)
			break
		else:
			print("Not Now:" )
			pass
			time.sleep(1)
		pass

def get_if_good_minute(given_t:datetime) -> None:
	"""
	特定の時間になると、時間を表示する関数。
	"""
	current_t = datetime.datetime.now()
	if (if_equal_time(current_t, given_t)):
		today = current_time.strftime('%m月%d日%I:%M')
		print("CURRENT_TIME: " + today)
	else:
		print("Not Now:")