from config.constants import MONTH_ABRS, WEEK_DAY_ABRS

# Tuple [day_count, month_abbr, year]
OwnDate = tuple[int, str, int]


def init_date(day, month_abr, year) -> OwnDate:
  if month_abr in MONTH_ABRS:
    return (day, month_abr, year)
  raise ValueError("var 'month_abr' should be from the list MONTH_ABRS")


def init_date_with_month_num(day, month_num, year) -> OwnDate:
  if month_num in [i for i in range(len(MONTH_ABRS))]:
    month_abr = MONTH_ABRS[month_num]
    return (day, month_abr, year)
  raise ValueError("var 'month_num' should be from the range of len(MONTH_ABRS)")


def get_day_num(date: OwnDate) -> int:
  return date[0]


def get_week_day_num(week_abr) -> int:
  return WEEK_DAY_ABRS.index(week_abr)


def get_month_num(date: OwnDate) -> int:
  return MONTH_ABRS.index(date[1])


def get_month_num_from_abr(month_abr: str) -> int:
  return MONTH_ABRS.index(month_abr)


def get_month_abr_from_num(month_num: int) -> str:
  return MONTH_ABRS[month_num]


def get_month_abr(date: OwnDate) -> str:
  return date[1]


def get_year_num(date: OwnDate) -> int:
  return date[2]
