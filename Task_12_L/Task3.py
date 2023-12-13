'''
2. Создаём итераторы
Список list можно передать в цикл for in для перебора его элементов, итерации.
Также итерироваться по списку можно в генераторных выражениях. А можно
передать список функции для итерации, например функции all(). У итерируемых
объектов много способов использования. Можно ли создать итерируемый объект
самому? Да. Если экземпляр класса должен итерироваться, необходимо
реализовать пару дандер методов.
Создадим класс экземпляр которого будет выдавать числа Фибоначчи в диапазоне
начиная с числа больше или равного start и заканчивая числом меньше stop.
'''

class Fibonacci:
    def __init__(self, start, stop):
       self.start = start
       self.stop = stop
       self.first = 0
       self.second = 1

    # def __iter__(self):
    #     return self

    # Две строки метода вернули ссылку на самого себя. В результате получаем новую
    # ошибку. Вернулся не итерируемый объект.



fib = Fibonacci(20, 100)
for num in fib: # TypeError: 'Fibonacci' object is not iterable
    print(num)


'''Внутри дандер __init__ запомнили границы start и stop и определили нулевое и
первое число Фибоначчи в свойствах first и second соответственно.
Создание экземпляра не вызывает проблем. А попытка получить числа в цикле
увенчалась ошибкой. Python сообщил, что объект не итерируемый.

Возврат итератора, __iter__
Для того, чтобы объект стал итерируемым, ему необходимо вернуть
объект-итератор. В нашем случае экземпляр класса и есть объект-итератор.
Следовательно он должен вернуть сам себя. Для возврата итератора нужно создать
дандер метод __iter__.

'''