import datetime

TODAY = str(datetime.date.today())
DEFAULT_PROJECT = "inbox"
RECUR_CHOICES = ["daily", "weekly", "sun", "mon", "tue", "wed", "thur", "fri", "sat"]
DATE_FORMATS = ['%d-%m-%y', '%d-%m-%Y', '%d.%m.%y', '%d.%m.%Y', "%d/%m/%y", "%d/%m/%Y", "%Y-%m-%d"]
TIME_FORMATS = ['%H:%M', '%I:%M%p']

# ANSI colors
GREEN = '\u001b[32m'
RED = '\u001b[31m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m' # this reset color not a actual color


HEADER_COLOR = 'blue' # only name like red, blue, green and yellow
PAST_COLOR = RED
PRESENT_COLOR = GREEN
FUTURE_COLOR = BLUE
TABLE_FORMAT = 'fancy_grid' # https://pypi.org/project/tabulate/ for more formats

