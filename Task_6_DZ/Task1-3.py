


def validate_date(date_to_prove):
    day, month, year = date_to_prove.split('.')

    try:
        day = int(day)
        month = int(month)
        year = int(year)

        if month < 1 or month > 12:
            return False

        if day < 1:
            return False

        if month in [4, 6, 9, 11] and day > 30:
            return False

        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                if day > 29:
                    return False
            elif day > 28:
                return False

        if day > 31:
            return False

        return True

    except ValueError:
        return False


# Пример использования
# date_to_prove = input("Введите дату в формате 'день.месяц.год': ")
date_to_prove = '12.4.-2023'
result = validate_date(date_to_prove)
print(result)