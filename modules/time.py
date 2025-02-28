from modules.own_time import OwnTime, init_time, init_utc_time_h, init_utc_time_hm, init_utc_time_hms, get_hours, get_minutes, get_seconds


def to_unix_time_stamp(time: OwnTime) -> int:
  return time[2] + 60 * time[1] + 60 * 60 * time[0]


def to_unix_time_stamp_from_utc(time: OwnTime) -> int:
  return to_unix_time_stamp(time) + 60 * time[4] + 60 * 60 * time[3]


def get_interval_in_seconds(start: OwnTime, end: OwnTime) -> OwnTime:
  return to_unix_time_stamp_from_utc(end) - to_unix_time_stamp_from_utc(start)
