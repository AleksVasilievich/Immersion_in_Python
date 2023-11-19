'''
Задание
Перед вами несколько строк кода. Что будет записано в файл после его
выполнения? У вас три минуты.
'''

import pickle

my_dict = {'numbers': [42, 4.1415, (7 + 3j)],
           'functions': (sum, max),
           'others': {False, True, 'Hello world!'}
           }
res = pickle.dumps(my_dict)
with open('quest.pickle', 'wb') as f:
    pickle.dump(f'{res = }', f)
