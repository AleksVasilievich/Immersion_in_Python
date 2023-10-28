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


def count_words(text):
    # Знаки препинания
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    # Приводим текст к нижнему регистру
    text = text.lower()

    # Удаляем знаки препинания из текста
    for char in punctuation:
        text = text.replace(char, ' ')

    # Разбиваем текст на отдельные слова
    words = text.split()

    # Подсчитываем количество повторяющихся слов
    word_counts = {}

    for word in words:
        # Удаляем апострофы из слов
        word = word.strip("'")

        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Возвращаем 10 самых часто встречаемых слов
    most_common = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    return most_common
text = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."

# text = "Python 3.9 is the latest version of Python. It's awesome!"
# text = 'Hello world. Hello Python. Hello again.'
result = count_words(text)
print(result)

# проверку не прошол