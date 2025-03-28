from modules.own_date import init_date
from modules.own_time import init_time

from modules.print import print_quarter

day = init_date(28, "MAR", 2025)
time = init_time(0, 0, 0, 0, 0)

print_quarter(day)
