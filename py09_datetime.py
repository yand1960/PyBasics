import datetime as dt

# now = dt.datetime.now()
# print(now)

# today = dt.date.today()
# print(today)

# Сколько дней осталось до Нового Года?
# today = dt.date.today()
# newYear = dt.date(today.year + 1 ,1,1)
# tillNewYear = newYear - today
# daysLeft = tillNewYear.days
# print(f"До НГ осталось {daysLeft} дн.")

# Оформите вычисление числа дней, оставшихся до НГ в виде функции
# и протестриуйте ее

def daysTillNewYear():
    today = dt.date.today()
    newYear = dt.date(today.year + 1 ,1,1)
    tillNewYear = newYear - today
    daysLeft = tillNewYear.days
    return daysLeft

print(f"До НГ осталось {daysTillNewYear()} дн.")

def daysTillNewYearFromStatusDate(statusDate = dt.date.today()):
    newYear = dt.date(statusDate.year + 1 ,1,1)
    tillNewYear = newYear - statusDate
    daysLeft = tillNewYear.days
    return daysLeft

print(f"До НГ осталось {daysTillNewYearFromStatusDate(statusDate = dt.date(2022,1,1))} дн.")
print(f"До НГ осталось {daysTillNewYearFromStatusDate()} дн.")

