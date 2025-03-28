from config.constants import BEGIN_DAY, LEAP_YEAR, BEGIN_DATE, SECONDS_IN_24H, MONTH_ABRS, WEEK_DAY_ABRS
from modules.own_date import OwnDate, init_date, init_date_with_month_num, get_day_num, get_week_day_num, get_week_day_abr, get_month_num, get_month_num_from_abr, get_month_abr_from_num, get_month_abr, get_year_num


# Get leap year or not
def is_leap_year(year: int) -> bool:
  return abs(year - LEAP_YEAR) % 4 == 0


# Get count of year's days
def get_year_day_count(year: int) -> int:
  return 365 + (1 if is_leap_year(year) else 0)


# Get count of month's days
def get_month_day_count(month_abr: str, year: int) -> int:
  big_month_numbers = [ 0, 2, 4, 6, 7, 9, 11 ]
  if get_month_num_from_abr(month_abr) == 1:
    return 28 + (1 if is_leap_year(year) else 0)
  elif get_month_num_from_abr(month_abr) in big_month_numbers:
    return 31
  else:
    return 30


# Get week day number with offset
def get_week_day_with_offset(start_day_abr: str, offset: int) -> int:
  return (get_week_day_num(start_day_abr) + offset % len(WEEK_DAY_ABRS)) % len(WEEK_DAY_ABRS)


# Get day number of a year
def get_day_of_year(date: OwnDate) -> int:
  output_day = get_day_num(date)
  for m in range(0, get_month_num(date)):
    output_day += get_month_day_count(get_month_abr_from_num(m), get_year_num(date))
  return output_day


# Get day count between two dates
def get_interval_in_days(start: OwnDate, end: OwnDate) -> int:
  day_count = 0
  start_year = min(get_year_num(start), get_year_num(end))
  end_year = max(get_year_num(start), get_year_num(end))
  for y in range(start_year, end_year):
    day_count += get_year_day_count(y)
  day_count += get_day_of_year(end) - get_day_of_year(start)
  return day_count if get_year_num(end) >= get_year_num(start) else -1 * day_count


# Get week day number of any day
def get_week_day(date: OwnDate) -> int:
  day_count = get_interval_in_days(BEGIN_DATE, date)
  return get_week_day_with_offset(BEGIN_DAY, day_count)


# Get week number of a year
def get_week_of_year(date: OwnDate) -> int:
  day_number = get_day_of_year(date)
  first_day_of_current_year = (1, date[1], date[2])
  day_number_without_first_week = day_number - (len(WEEK_DAY_ABRS) - get_week_day(first_day_of_current_year))
  return day_number_without_first_week // len(WEEK_DAY_ABRS) + 2


# Get amount of seconds of date's 00:00:00 from BEGIN_DATE's 00:00:00
def get_midnight_seconds(date: OwnDate) -> int:
  day_count = get_interval_in_days(BEGIN_DATE, date)
  return SECONDS_IN_24H * day_count


# Get OwnDate from day of year
def get_date_from_day_of_year(day_num: int, year: int) -> OwnDate:
  offset = day_num
  for m in range(len(MONTH_ABRS)):
    month_day_count = get_month_day_count(MONTH_ABRS[m], year)
    if offset - month_day_count <= 0:
      return init_date(offset, MONTH_ABRS[m], year)
    else:
      offset -= month_day_count


# Add offset in months and returns new date and year count offset
def add_month_offset(current_date: OwnDate, interval_in_month: int) -> tuple[OwnDate, int]:
  current_month_num = get_month_num(current_date)
  current_year_num = get_year_num(current_date)
  new_day_num = get_day_num(current_date)
  new_month_num = (current_month_num + interval_in_month) % len(MONTH_ABRS)
  new_year_num = (current_month_num + interval_in_month) // len(MONTH_ABRS)
  new_date = init_date_with_month_num(new_day_num, new_month_num, current_year_num + new_year_num)
  return new_date, new_year_num


# Add offset in days and returns new date and month count offset
def add_days_offset(current_date: OwnDate, interval_in_days: int) -> tuple[OwnDate, int]:
  year_num = get_year_num(current_date)
  current_year_day_count = get_year_day_count(year_num)
  current_year_day = get_day_of_year(current_date)
  offset = current_year_day + interval_in_days
  if offset < 0:
    new_year = year_num
    while offset < 0:
      new_year -= 1
      previous_year_day_count = get_year_day_count(new_year)
      offset += previous_year_day_count
    new_date = get_date_from_day_of_year(offset, new_year)
    return new_date, get_month_num(new_date) - get_month_num(current_date) - (year_num - new_year) * len(MONTH_ABRS)
  elif offset > current_year_day_count:
    new_year = year_num
    while offset > 0:
      new_year += 1
      next_year_day_count = get_year_day_count(new_year)
      offset -= next_year_day_count
    new_date = get_date_from_day_of_year(offset, new_year)
    return new_date, get_month_num(new_date) - get_month_num(current_date) + (year_num - new_year) * len(MONTH_ABRS)
  else:
    new_date = get_date_from_day_of_year(offset, year_num)
    return new_date, get_month_num(new_date) - get_month_num(current_date)


def get_week_of_date(date: OwnDate) -> tuple[int]:
  """Get week dates of the requested day

  Args:
    date (OwnDate): date of requested day
  
  Returns:
    Tuple[int]: a set of week dates of the requested day (if week contains dates from other month the value will be `0`)
  """
  current_month = get_month_abr(date)
  current_year = get_year_num(date)
  current_week_day = get_week_day(date)
  day_count_of_current_month = get_month_day_count(current_month, current_year)
  first_day_of_current_week, month_offset = add_days_offset(date, -1 * current_week_day)
  first_week_day = get_week_day(first_day_of_current_week)
  week = []
  if month_offset == 0:
    first_week_day = get_day_num(first_day_of_current_week)
    for d in range(first_week_day, first_week_day + len(WEEK_DAY_ABRS), 1):
      if d <= day_count_of_current_month:
        week.append(d)
      else:
        week.append(0)
  elif month_offset < 0:
    transition_interval = get_interval_in_days(date, first_day_of_current_week)
    for d in range(transition_interval, 0):
      week.append(0)
    for d in range(len(WEEK_DAY_ABRS) + transition_interval):
      week.append(d + 1)
  elif month_offset > 0:
    transition_interval = get_interval_in_days(date, first_day_of_current_week)
    for d in range(transition_interval, current_week_day + 1, 1):
      if d + 1 <= 0:
        week.append(0)
      else:
        week.append(d + 1)
  return tuple(week)


def get_month_of_date(date: OwnDate) -> tuple[tuple[int]]:
  month = []
  day_of_month = init_date(1, get_month_abr(date), get_year_num(date))
  current_month_offset = 0
  while current_month_offset == 0:
    month.append(get_week_of_date(day_of_month))
    day_of_month, current_month_offset = add_days_offset(day_of_month, len(WEEK_DAY_ABRS))
  day_of_month, current_month_offset = add_days_offset(day_of_month, -1 * get_week_day(day_of_month))
  if current_month_offset == -1:
    month.append(get_week_of_date(day_of_month))
  return tuple(month)


def get_nearest_three_months(date: OwnDate) -> tuple[tuple[tuple[int]]]:
  quarter = []
  previous_date, _ = add_month_offset(date, -1)
  next_date, _ = add_month_offset(date, 1)
  previous_month = get_month_of_date(previous_date)
  current_month = get_month_of_date(date)
  next_month = get_month_of_date(next_date)
  previous_month_week_count = len(previous_month)
  current_month_week_count = len(current_month)
  next_month_week_count = len(next_month)
  empty_week = tuple([0 for _ in range(len(WEEK_DAY_ABRS))])
  for i in range(max(previous_month_week_count, current_month_week_count, next_month_week_count)):
    quarter.append((
      previous_month[i] if i < previous_month_week_count else empty_week,
      current_month[i] if i < current_month_week_count else empty_week,
      next_month[i] if i < next_month_week_count else empty_week,
    ))
  return tuple(quarter)

