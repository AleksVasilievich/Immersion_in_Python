"""
В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.

Слова разделяются пробелами, апостроф не считается за пробел.
Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.

Отсортируйте по убыванию значения количества повторяющихся слов.
Пример
На входе:    text = 'Hello world. Hello Python. Hello again.'
На выходе:   [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]
"""

import re
from collections import Counter

text1 = 'Hello world. Hello Python. Hello again.'
text2 = "Python 3.9 is the latest version of Python. It's awesome!"
text = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."


def count_words(text):
    # Удаляем знаки препинания и приводим текст к нижнему регистру
    # text = re.compile("(?<=\d)(\.)(\d)")
    text = re.sub(r'[^\w\s\']', '', text.lower())

    # Разбиваем текст на отдельные слова
    words = re.findall(r'\b\w+\b', text)

    # Подсчитываем количество повторяющихся слов
    word_counts = Counter(words)

    # Возвращаем 10 самых часто встречаемых слов
    most_common = word_counts.most_common(10)

    return most_common


result = count_words(text)
print(result)

#проверку не прошол