# Months lists
MONTHS_RU = [ "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь" ]
MONTHS_EN = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]
MONTHS_FR = [ "Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre" ]
MONTHS = {
  "EN": MONTHS_EN,
  "FR": MONTHS_FR,
  "RU": MONTHS_RU,
}

MONTH_NUMBER = { "JAN": 0, "FEB": 1, "MAR": 2, "APR": 3, "MAY": 4, "JUN": 5, "JUL": 6, "AUG": 7, "SEP": 8, "OCT": 9, "NOV": 10, "DEC": 11 }

# Weeks list
WEEK_RU = [ "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье" ]
WEEK_EN = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]
WEEK_FR = [ "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche" ]
WEEK = {
  "EN": WEEK_EN,
  "FR": WEEK_FR,
  "RU": WEEK_RU,
}

WEEK_NUMBER = { "MON": 0, "TUE": 1, "WED": 2, "THU": 3, "FRI": 4, "SAT": 5, "SUN": 6 }

# Begin date
BEGIN_DAY = 3 # Thursday
BEGIN_MONTH = 0 # January
BEGIN_YEAR = 1970
LEAP_YEAR = 1972

MIN_INTERVAL = 1


# Get leap year or not
# @param year - Number, full year
# @return Boolean
def is_leap_year(year):
  return abs(year - LEAP_YEAR) % 4 == 0


# Get count of month's days
# @param month - Number, month's number (from 0 up to 11 included)
# @param year - Number, full year
# @return Number
def get_month_day_count(month, year):
  big_month_numbers = [ 0, 2, 4, 6, 7, 9, 11 ]
  if month == 1:
    return 28 + (1 if is_leap_year(year) else 0)
  elif month in big_month_numbers:
    return 31
  else:
    return 30


# Get count of year's days
# @param year - Number, full year
# @return Number
def get_year_day_count(year):
  return 365 + (1 if is_leap_year(year) else 0)


# Get day number of a year
# @param day - Number, number of a day in a month
# @param month - Number, month's number (from 0 up to 11 included)
# @param year - Number, full year
# @return Number
def get_day_of_year(day, month, year):
  output_day = day
  for m in range(0, month):
    output_day += get_month_day_count(m, year)
  return output_day


# Get week day number with offset
# @param start_day - Number, day number of a week (from 0 up to 6 included)
# @param offset - Number, day count of offset (any integer number with any sign) 
# @return Number
def get_week_day_with_offset(start_day, offset):
  return (start_day + offset % 7) % 7


# Get week day number of any day
# @param day - Number, number of a day in a month
# @param month - Number, month's number (from 0 up to 11 included)
# @param year - Number, full year
# @return Number
def get_week_day(day, month, year):
  day_count = 0
  start_year = min(year, BEGIN_YEAR)
  end_year = max(year, BEGIN_YEAR)
  for y in range(start_year, end_year):
    day_count += get_year_day_count(start_year + y)
  if year >= BEGIN_YEAR:
    day_count += get_day_of_year(day, month, year)
    return get_week_day_with_offset(BEGIN_DAY, day_count - 1)
  else:
    day_count -= get_day_of_year(day, month, year)
    return get_week_day_with_offset(BEGIN_DAY, -1 * (day_count + 1))


# Get week number of a year
# @param day - Number, number of a day in a month
# @param month - Number, month's number (from 0 up to 11 included)
# @param year - Number, full year
# @return Number
def get_week_of_year(day, month, year):
  day_number = get_day_of_year(day, month, year)
  day_number_without_first_week = day_number - (7 - get_week_day(1, MONTH_NUMBER["JAN"], year))
  return day_number_without_first_week // 7 + 2

print(get_week_of_year(21, MONTH_NUMBER["FEB"], 2025))
