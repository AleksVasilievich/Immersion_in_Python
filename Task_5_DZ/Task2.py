'''
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
 имена str, ставка int, премия str с указанием процентов вида 10.25%.
В результате result получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии.
Не забудьте распечатать в конце результат.
Пример использования.
На входе:                                    На выходе:    {'Alice': 500.0, 'Bob': 300.0, 'Charlie': 1050.0}

names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]
'''



names = ['Борис', 'Иван', 'Петр', "Сергей"]
salaries = [10000, 12000, 16000, 14000]
awards = ['12.35%', '10.25%', '7.75%', '8.85%']

def func1(lst_names, lst_bases, lst_bonuses):
    return {name: base * float(award.rstrip('%')) / 100 for name, base, award in zip(lst_names, lst_bases, lst_bonuses)}

print(func1(names, salaries, awards))


'''
Решение системы

result = {names[i]: round(salary[i] * float(bonus[i].strip('%')) / 100, 2) for i in range(len(names))}
print(result)

'''