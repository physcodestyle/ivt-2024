from config.constants import LANGUAGES, MONTHS, MONTH_NUMBER, WEEK, WEEK_NUMBER, BEGIN_DAY, BEGIN_YEAR, LEAP_YEAR, BEGIN_DATE
from modules.types import OwnDate, get_day_num, get_month_num, get_month_abr, get_year_num

# Get leap year or not
# @param year - Number, full year
# @return Boolean
def is_leap_year(year) -> bool:
  return abs(year - LEAP_YEAR) % 4 == 0


# Get count of month's days
# @param month_abr - String, first month's three symbols in uppercase
# @param year - Number, full year
# @return Number
def get_month_day_count(month_abr: str, year: int) -> int:
  big_month_numbers = [ 0, 2, 4, 6, 7, 9, 11 ]
  if MONTH_NUMBER[month_abr] == 1:
    return 28 + (1 if is_leap_year(year) else 0)
  elif MONTH_NUMBER[month_abr] in big_month_numbers:
    return 31
  else:
    return 30


# Get count of year's days
def get_year_day_count(year: int) -> int:
  return 365 + (1 if is_leap_year(year) else 0)


# Get day number of a year
def get_day_of_year(date: OwnDate) -> int:
  output_day = get_day_num(date)
  for m in range(0, get_month_num(date)):
    output_day += get_month_day_count(m, get_year_num(date))
  return output_day


# Get week day number with offset
def get_week_day_with_offset(start_day_abr: str, offset: int) -> int:
  return (WEEK_NUMBER[start_day_abr] + offset % 7) % 7

# Get day count between two dates
def get_interval_in_days(start: OwnDate, end: OwnDate) -> int:
  day_count = 0
  start_year = min(get_year_num(start), get_year_num(end))
  end_year = max(get_year_num(start), get_year_num(end))
  for y in range(start_year, end_year):
    day_count += get_year_day_count(start_year + y)
  day_count += get_day_of_year(end) - get_day_of_year(start)
  return day_count if get_year_num(end) >= get_year_num(start) else -1 * day_count


# Get week day number of any day
def get_week_day(date: OwnDate) -> int:
  day_count = get_interval_in_days(BEGIN_DATE, date)
  return get_week_day_with_offset(BEGIN_DAY, day_count)


# Get week number of a year
# @param day - Number, number of a day in a month
# @param month_abr - String, first month's three symbols in uppercase
# @param year - Number, full year
# @return Number
def get_week_of_year(day: int, month_abr: str, year: int) -> int:
  day_number = get_day_of_year(day, MONTH_NUMBER[month_abr], year)
  day_number_without_first_week = day_number - (7 - get_week_day(1, MONTH_NUMBER["JAN"], year))
  return day_number_without_first_week // 7 + 2

