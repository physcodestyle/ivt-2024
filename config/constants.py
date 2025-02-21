LANGUAGES = [ "EN", "FR","RU" ]

# Months lists
MONTHS_RU = [ "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь" ]
MONTHS_EN = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]
MONTHS_FR = [ "Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre" ]
MONTHS = {
  "EN": MONTHS_EN,
  "FR": MONTHS_FR,
  "RU": MONTHS_RU,
}

MONTH_NUMBER = { "JAN": 0, "FEB": 1, "MAR": 2, "APR": 3, "MAY": 4, "JUN": 5, "JUL": 6, "AUG": 7, "SEP": 8, "OCT": 9, "NOV": 10, "DEC": 11 }

# Weeks list
WEEK_RU = [ "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье" ]
WEEK_EN = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]
WEEK_FR = [ "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche" ]
WEEK = {
  "EN": WEEK_EN,
  "FR": WEEK_FR,
  "RU": WEEK_RU,
}

WEEK_NUMBER = { "MON": 0, "TUE": 1, "WED": 2, "THU": 3, "FRI": 4, "SAT": 5, "SUN": 6 }

# Begin date
BEGIN_YEAR = 1970
LEAP_YEAR = 1972
BEGIN_DATE = (1, "JAN", BEGIN_YEAR)
BEGIN_DAY = "THU"
