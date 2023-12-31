'''
3. Создаём менеджер контекста with
Менеджер контекста with запускает два дандер метода. Один в момент вызова
менеджера, а второй в момент выхода из внутреннего блока кода. Знакомая нам
функция open() поддерживает работу с менеджером контекста. При вызове
менеджера функция возвращает файловый дескриптор. А при выходе из него
закрывает файл. Подобный функционал можно реализовать для любого объекта,
где нужны одинаковые действия в начале и в конце. Рассмотрим пример работы с
базой данных sqlite.
'''

import sqlite3


connection = sqlite3.connect('sqlite.db')
cursor = connection.cursor()
cursor.execute("""create table if not exists users(name,age);""")
cursor.execute("""insert into users values ('Гвидо', 66);""")
connection.commit()
connection.close()
