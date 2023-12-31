'''
В этом безобидном примере модуль получил доступ к консоли и вывел сообщение
“Привет, мир!” прежде чем десериализовать поток байт в число ноль.
'''

import pickle
import  os

res = pickle.loads(b"cos\nsystem\n(S'echo Hello world!'\ntR.")
print(res)

os.system('echo Hello World!')

'''
Допустимые типы данных
для преобразования
Модуль pickle может обработать следующие структуры Python:
● None, True и False;
● int, float, complex;
● str, bytes, bytearrays;
● tuple, list, set, dict если они содержат объекты, обрабатываемые pickle;
● встроенные функции и функции созданные разработчиком и доступные из
верхнего уровня модуля, кроме lambda функций;
● классы доступные из верхнего уровня модуля;
● экземпляры классов, если pickle смог обработать их дандер __dict__ или
результат вызова метода __getstate__().
Список достаточно большой, чтобы позволить сериализовывать большую часть
Python структур.
'''