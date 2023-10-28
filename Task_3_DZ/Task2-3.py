def count_words(text):
    # Знаки препинания
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    # Приводим текст к нижнему регистру
    text = text.lower()

    # Удаляем знаки препинания из текста
    for char in punctuation:
        text = text.replace(char, '')

    # Разбиваем текст на отдельные слова
    words = text.split()

    # Обрабатываем слова с числами
    processed_words = []
    for word in words:
        # Если слово содержит точку и состоит из цифр, объединяем его в одно слово
        if '.' in word and word.replace('.', '').isdigit():
            processed_words.append(word.replace('.', ''))
        else:
            processed_words.append(word)

    # Подсчитываем количество повторяющихся слов
    word_counts = {}

    for word in processed_words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Возвращаем 10 самых часто встречаемых слов
    most_common = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    # return most_common
    print(most_common)

text = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."

# text = "Python 3.9 is the latest version of Python. It's awesome!"
# result = count_words(text)
# print(result)

count_words(text

# проверку не прошол
