'''
● Действия при входе в менеджер контекста, __enter__
Создадим класс DB для упрощения работы с базой данных.

● Действия при выходе из менеджера контекста, __exit__
Добавим дандер метод __exit__ и пропишем в нём операции, обязательные при
завершении работы с базой данных
'''


import sqlite3
class DB:
    def __init__(self, name):
         self.name = name
         self.connection = None
         self.cursor = None
    def __enter__(self):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        return self.cursor
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
        self.cursor = self.connection = None





db = DB('sqlite.db')
with db as cur:
    cur.execute("""create table if not exists users(name, age);""")
    cur.execute("""insert into users values ('Гвидо', 66);""")