from config.constants import MONTH_NUMBER

OwnDate = tuple[int, str, int]

def get_day_num(date: OwnDate) -> int:
  return date[0]

def get_month_num(date: OwnDate) -> int:
  return MONTH_NUMBER[date[1]]

def get_month_abr(date: OwnDate) -> str:
  return date[1]

def get_year_num(date: OwnDate) -> int:
  return date[2]