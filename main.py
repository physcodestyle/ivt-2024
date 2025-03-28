from modules.own_date import init_date
from modules.own_time import init_time

# from modules.own_date import OwnDate, get_day_num, get_month_abr, get_year_num, get_week_day_num
# from modules.date import get_month_day_count, get_week_day, add_days_offset
from modules.date import get_week_of_date, get_month_of_date

day = init_date(28, "MAR", 2025)
time = init_time(0, 0, 0, 0, 0)

print(get_week_of_date(day))
print(get_month_of_date(day))
