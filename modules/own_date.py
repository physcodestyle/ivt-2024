MONTHS = [ "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC" ]
WEEK = [ "MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN" ]

# Tuple [day_count, month_abbr, year]
OwnDate = tuple[int, str, int]


def init_date(day, month_abr, year) -> OwnDate:
  if month_abr in MONTHS:
    return (day, month_abr, year)
  raise ValueError("var 'month_abr' should be from the list MONTHS")


def get_day_num(date: OwnDate) -> int:
  return date[0]


def get_week_day_num(week_abr) -> int:
  return WEEK.index(week_abr)


def get_month_num(date: OwnDate) -> int:
  return MONTHS.index(date[1])


def get_month_abr(date: OwnDate) -> str:
  return date[1]


def get_year_num(date: OwnDate) -> int:
  return date[2]
