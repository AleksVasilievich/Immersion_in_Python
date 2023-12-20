from datetime import datetime, timedelta
import calendar

"""
Задание №4.
Функция получает на вход текст вида: “1-й четверг ноября”, “3-
я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответствует формату.
"""


def convert_text_to_date(text):
    parts = text.split()
    # Словарь для преобразования порядковых номеров в числовые значения
    ordinal_numbers = {'1st': 1, '2nd': 2, '3rd': 3, '4th': 4, '5th': 5}
    try:
        # получим порядковый номер и день недели из входного текста
        ordinal = ordinal_numbers[parts[0].lower()]
        weekday = parts[1].capitalize()
        month = parts[3].capitalize()

        # получим текущий год
        current_year = datetime.now().year
        # найдём индекс дня недели (0-6) используя модуль calendar
        weekday_index = list(calendar.day_name).index(weekday)
        # найдём первое появление дня недели в месяце
        dt = datetime(current_year, datetime.strptime(month, '%B').month, 1)

        while dt.weekday() != weekday_index:
            dt += timedelta(days=1)

        # прибавляем смещение в днях
        dt += timedelta(days=(ordinal - 1) * 7)
        return dt
    except (ValueError, IndexError, KeyError) as e:
        # Добавить логирование
        print(f'Ошибка: {e}')
        return None