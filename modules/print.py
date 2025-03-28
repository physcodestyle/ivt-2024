from config.constants import MONTH_ABRS, WEEK_DAY_ABRS
from modules.own_date import OwnDate, get_day_num
from modules.date import get_week_of_date, get_month_of_date, get_nearest_three_months

def print_quarter(date: OwnDate):
  quarter = get_nearest_three_months(date)
  pattern = "{:s}\t{:s}\t{:s}\t{:s}\t{:s}\t{:s}\t{:s}\t\t{:s}\t{:s}\t{:s}\t{:s}\t{:s}\t{:s}\t{:s}\t\t{:s}\t{:s}\t{:s}\t{:s}\t{:s}\t{:s}\t{:s}"
  output = pattern.format(*(WEEK_DAY_ABRS + WEEK_DAY_ABRS + WEEK_DAY_ABRS))
  print(output)
  for i in range(len(quarter)):
    line = []
    for j in range(3):
      for k in range(len(quarter[i][j])):
        day = str(quarter[i][j][k])
        if j == 1 and quarter[i][j][k] == get_day_num(date):
          day += ' <'
        line.append(day if quarter[i][j][k] != 0 else '')
    output = pattern.format(*line)
    print(output)