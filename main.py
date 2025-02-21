from config.constants import WEEK
from modules.days import get_week_day

day = (1, "JAN", 1970)
print(WEEK["RU"][get_week_day(day)])