from modules.own_date import init_date
from modules.own_time import init_time
from modules.time import add_seconds_offset


day = init_date(1, "JAN", 1970)
time = init_time(0, 0, 0, 0, 0)

print(60 * 60 * 24)
print(60 * 60 * 24 - 60 * 60)
print(add_seconds_offset(time, 60 * 60 * -15))