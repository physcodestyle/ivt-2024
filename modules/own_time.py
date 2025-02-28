SECOND_LIMIT = (0, 59)
MINUTE_LIMIT = (0, 59)
HOUR_LIMIT = (0, 23)
TZ_MINS_VALUES = (0, 30, 45)
TZ_HRS_VALUES = (-12, 14)


# Tuple [hours, minutes, seconds, timezone_hours (UTC), timezone_minutes (UTC)]
OwnTime = tuple[int, int, int, int, int]


def init_time(hours, minutes, seconds, timezone_hours, timezone_minutes) -> OwnTime:
  if isinstance(hours, int) and hours <= HOUR_LIMIT[0] and hours >= HOUR_LIMIT[1]:
    raise ValueError("'hours' is out of range or not integer")
  elif isinstance(minutes, int) and minutes <= MINUTE_LIMIT[0] and minutes >= MINUTE_LIMIT[1]:
    raise ValueError("'minutes' is out of range or not integer")
  elif isinstance(seconds, int) and seconds < SECOND_LIMIT[0] and seconds > SECOND_LIMIT[1]:
    raise ValueError("'seconds' is out of range or not integer")
  elif isinstance(timezone_hours, int) and timezone_hours < TZ_HRS_VALUES[0] and timezone_hours > TZ_HRS_VALUES[1]:
    raise ValueError("'timezone_hours' is out of range or not integer")
  elif isinstance(timezone_minutes, int) and timezone_minutes not in TZ_MINS_VALUES:
    raise ValueError("'timezone_minutes' is out of range or not integer")
  else:
    return (hours, minutes, seconds, timezone_hours, timezone_minutes)


def init_utc_time_hms(hours, minutes, seconds) -> OwnTime:
  return init_time(hours, minutes, seconds, 0, 0)


def init_utc_time_hm(hours, minutes) -> OwnTime:
  return init_time(hours, minutes, 0, 0, 0)


def init_utc_time_h(hours) -> OwnTime:
  return init_time(hours, 0, 0)


def get_hours(time: OwnTime) -> int:
  return time[0]


def get_minutes(time: OwnTime) -> int:
  return time[1]


def get_seconds(time: OwnTime) -> int:
  return time[2]
  