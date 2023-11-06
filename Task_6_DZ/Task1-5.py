# Этот вариант прошёл проверку тэста

date_to_prove = "30.02.2020"

day, month, year = [int(i) for i in date_to_prove.split('.')]
leap_year = False
flag = True
if year % 4 == 0 and (year % 100 != 0 or year % 4 == 0):
    leap_year = True
if (day <  1 or day > 31) or (month < 1 or month > 12) or (year < 1 or year > 9999):
    flag = False
if leap_year == True and month == 2 and (day <  1 or day > 29):
    flag = False
elif leap_year == False and month == 2 and (day <  1 or day > 28):
    flag = False
print(flag)
