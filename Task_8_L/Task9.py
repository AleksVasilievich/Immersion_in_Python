'''
🔥 Важно! При работе с CSV необходимо указывать параметр newline=’’ во
время открытия файла.
Кроме файлового дескриптора можно передать любой объект поддерживающий
итерацию и возвращающий строки. Также функция reader может принимать
диалект отличный от заданного по умолчанию — “excel”. А при необходимости и
дополнительные параметры форматирования, если файл имеет свои особенности.
Файл biostats_tab.csv хранит те же данные, что и файл выше, но вместо разделителя
используется символ табуляции. По сути это разновидность TSV — файл с
разделителем табуляцией.
"Name" "Sex" "Age" "Height (in)" "Weight (lbs)"
"Alex" "M" 41 74 170
"Bert" "M" 42 68 166
"Carl" "M" 32 70 155
"Dave" "M" 39 72 167
"Elly" "F" 30 66 124
"Fran" "F" 33 66 115
"Gwen" "F" 26 64 121
"Hank" "M" 30 71 158
"Ivan" "M" 53 72 175
"Jake" "M" 32 69 143
"Kate" "F" 47 69 139
"Luke""M" 34 72 163
"Myra" "F" 23 62 98
"Neil" "M" 36 75 160
"Omar" "M" 38 70 145
"Page" "F" 31 67 135
"Quin""M" 29 71 176
"Ruth""F" 28 65 131
Добавим несколько параметров для его чтения
➢ dialect='excel-tab' — указали диалект с табуляцией в качестве разделителя
➢ quoting=csv.QUOTE_NONNUMERIC — передали встроенную константу,
указывающую функции, что числа без кавычек необходимо преобразовать к
типу float.
'''

import csv

with open('biostats_tab.csv', 'r', newline='') as f:
    csv_file = csv.reader(f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(line)
    print(type(line))


# import csv
#
# with open('biostats_tab.csv', 'r', newline='') as f:
#     csv_file = csv.reader(f, delimiter='\t')
#     header = next(csv_file)
#     print(header)
#     for line in csv_file:
#         line = [item if not item.isdigit() else int(item) for item in line]
#         print(line)