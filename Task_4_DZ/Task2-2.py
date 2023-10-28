def key_params(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if hashable(key):
            result[value] = key
        else:
            result[str(value)] = key
    return result

def hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False

# Пример использования
params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)