import datetime

TODAY = datetime.datetime.now().strftime('%d-%m-%y')
DEFAULT_PROJECT = "inbox"
RECUR_CHOICES = ["daily", "weekly", "weekend", "sunday", "monday"]
DATE_FORMATS = ['%d-%m-%y', '%d-%m-%Y', '%d.%m.%y', '%d.%m.%Y']