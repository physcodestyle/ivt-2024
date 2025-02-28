from modules.own_time import OwnTime, init_time, init_utc_time_h, init_utc_time_hm, init_utc_time_hms, get_hours, get_minutes, get_seconds


SECONDS_IN_MINUTE = 60
SECONDS_IN_HOURS = 60 * 60
MAX_SECONDS_IN_24H = 60 * 60 * 24


def to_hms(seconds_from_midnight: int) -> tuple[int, int, int]:
  hours = seconds_from_midnight // SECONDS_IN_HOURS
  minutes = (seconds_from_midnight % SECONDS_IN_HOURS) // SECONDS_IN_MINUTE
  seconds = (seconds_from_midnight % SECONDS_IN_HOURS) % SECONDS_IN_MINUTE
  return (hours, minutes, seconds)


def to_own_time(seconds_from_midnight: int, timezone_hours: int, timezone_minutes: int) -> OwnTime:
  hours, minutes, seconds = to_hms(seconds_from_midnight)
  return init_time(hours, minutes, seconds, timezone_hours, timezone_minutes)


def to_own_time_utc(seconds_from_midnight: int) -> OwnTime:
  hours, minutes, seconds = to_hms(seconds_from_midnight)
  return init_utc_time_hms(hours, minutes, seconds)


def to_unix_time_stamp(time: OwnTime) -> int:
  return time[2] + SECONDS_IN_MINUTE * time[1] + SECONDS_IN_HOURS * time[0]


def to_unix_time_stamp_from_utc(time: OwnTime) -> int:
  return to_unix_time_stamp(time) + SECONDS_IN_MINUTE * time[4] + SECONDS_IN_HOURS * time[3]


def get_interval_in_seconds(start: OwnTime, end: OwnTime) -> OwnTime:
  return to_unix_time_stamp_from_utc(end) - to_unix_time_stamp_from_utc(start)


def add_seconds_offset(current_time: OwnTime, interval_in_seconds: int) -> tuple[OwnTime, int]:
  raw_time_in_seconds = to_unix_time_stamp(current_time) + interval_in_seconds
  new_time_in_seconds = raw_time_in_seconds % MAX_SECONDS_IN_24H
  day_offset = raw_time_in_seconds // MAX_SECONDS_IN_24H
  return (new_time_in_seconds, day_offset)
