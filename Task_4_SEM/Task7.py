"""
Задание №7
✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
"""

company_dist = {
    "Nokia": [10000, 8000],
    "Samsung": [15000, 12000],
    "Soyuz": [2000, 3000],
    "Huanmuan": [25000, 4000],
}

def check_profit(companies):
    res = {k: sum(v) for k, v in companies.items()}
    # print(res)
    if all(map(lambda x: x > 0, res.values())):
        return True
    return False


print(check_profit(company_dist))


def task_7(dat: dict):
    for el in dat.values():
        if sum(el) < 0:
            return False
    return True

print(task_7(company_dist))