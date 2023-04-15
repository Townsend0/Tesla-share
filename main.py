from data import *
import datetime

if datetime.datetime.now().weekday() in range(5):
	a = Stock()
	a.days()
	a.get_news()
	a.get_info()
	a.dif()
	a.send_not()