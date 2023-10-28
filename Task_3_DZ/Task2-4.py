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

def count_words(text):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    text = text.lower()

    p = re.compile("(\d)")
    text = p.sub("", text)

    for char in punctuation:
        text = text.replace(char, ' ')

    words = text.split()
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    most_common = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    # most_common = word_counts.items()
    print(most_common)

text = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."
text1 = "Python 3.9 is the latest version of Python. It's awesome!"
count_words(text)

#проверку прошол



# Решение системы
# import re
# from collections import Counter
#
# # Удаляем знаки препинания и приводим текст к нижнему регистру
# cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)
#
# # Разбиваем текст на слова и считаем их количество
# words = cleaned_text.split()
# word_counts = {}
#
# for word in words:
#     if word not in word_counts:
#         word_counts[word] = 1
#     else:
#         word_counts[word] += 1
#
# # Получаем 10 самых часто встречающихся слов
# top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]
#
# print(top_words)
