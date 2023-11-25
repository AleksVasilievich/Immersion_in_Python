'''
MRO
Аббревиатура MRO — method resolution order переводится как “порядок разрешения
методов”. Относится этот порядок не только к методам, но и ко всем атрибутам
класса. Это внутренний механизм, определяющий порядок наследования.
Забегая вперёд, иногда механизм не справляется с задачей. И чаще всего это
говорит о сложности кода и неверной логики построения наследования. Т.е.
нерабочий механизм наследования намекает разработчику на проблемы в его коде.
Рассмотрим работу MRO на нескольких простых классах.
'''


class A:
    def __init__(self):
        print('Init class A')
        self.data_a = 'A'


class B:
    def __init__(self):
        print('Init class B')
        self.data_b = 'B'


class C:
    def __init__(self):
        print('Init class C')
        self.data_c = 'C'


class D:
    def __init__(self):
        print('Init class D')
        self.data_d = 'D'


class X1(A, C):
    def __init__(self):
        print('Init class X1')
        super().__init__()


class X2(B, D):
    def __init__(self):
        print('Init class X2')
        super().__init__()


class X3(A, D):
    def __init__(self):
        print('Init class X3')
        super().__init__()


class Z(X1, X2, X3):
    def __init__(self):
        print('Init class Z')
        super().__init__()


print(*Z.mro(), sep='\n')


'''
1. Четыре класса A, B, C, D не имеют родительского класса. Точнее они
наследуются от прародителя object. У каждого из классов есть по параметру.
2. Далее три класса X имеют по два родительских класса.
3. В финале класс Z наследуется от трёх классов X.
У каждого класса добавили текстовый вывод при вызове методу __init__. Также
обратите внимание на наличие функции super, которая вызывает инициализацию
родительского класса.
У каждого класса есть метод mro, который вычисляет порядок наследования. Он
отвечает за инициализацию каждого класса один раз в порядке слева направо и по
старшинству, т.е. родитель не может быть инициализирован раньше дочернего
класа.. Подробнее про то как работает “монотонная линеаризация суперкласса”
можно прочитать по ссылке.
Разберём результат работы mro с нашим классом Z.
● В первую очередь отрабатывает инициализация самого класса.
● Далее начинаем двигаться слева направо по списку родительских классов:
X1, X2
● Следующим будет класс B. Почему он, а не X3? Класс B является
родительским только для класса X2. Так мы не нарушаем порядок слева
направо и старшинство.
● Следующим инициализируется X3, последний из родительских классов у Z.
23
● Далее идёт инициализация класса A. Он родитель для X1 и X3. Следовательно
его инициализация была невозможна раньше дочерних классов.
● Классы С и D инициализируются последними, они правее A, B и С в списке
родительских классов у “иксов”.
● Класс object всегда инициализируется в последнюю очередь.
Поиск аргументов и методов в экземпляре класса Z будет происходить в порядке,
представленном методом mro.
Добавим несколько строк кода и посмотрим на результат:

z = Z()
print(f'{z.data_b = }')
print(f'{z.data_a = }') # AttributeError: 'Z' object has no attribute 'data_a'

Вызов метода __init__ остановился на классе B. Мы не дописали ему вызов super,
считая что он и так не имеет наследников. В результате аргумент data_a не был
создан в экземпляре класса z. Попробуем описать классу A дополнительный метод.

class A:
    def __init__(self):
        print('Init class A')
        self.data_a = 'A'
    def say(self):
        print('Текст')
        print(self.data_b)
    ...
    
z = Z()
z.say()

Вызов метода say из класса A отработал без ошибок. Мы нашли его двигаясь по
цепочке линеаризации. При этом метод даже смог обратиться к свойству другого
класса. Связано это с тем, что мы работаем из экземпляра класса Z и он собрал в
себя аргументы и методы наследуемых классов.
🔥 Важно! Не стоит из родительских классов обращаться к аргументам и
методам дочерних классов или классов того же уровня наследования.
'''