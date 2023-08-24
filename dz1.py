# Создать декоратор для использования кэша. 
# Т.е. сохранять аргументы и результаты в словарь, если вызывается функция с агрументами, 
# которые уже записаны в кэше - вернуть результат из кэша, если нет - выполнить функцию. 
# Кэш лучше хранить в json.
# Решение, близкое к решению данной задачи было разобрано на семинаре.

import json
from functools import wraps

def cache_decorator(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = json.dumps([args, kwargs])
        
        if key in cache:
            print("Результат из кэша.")
            return cache[key]
        
        result = func(*args, **kwargs)
        cache[key] = result

        with open('cache.json', 'w') as file:
            json.dump(cache, file)
        
        print("Функция выполнена и результат кэширован.")
        return result
    
    try:
        with open('cache.json', 'r') as file:
            cache = json.load(file)
    except FileNotFoundError:
        cache = {}
    
    return wrapper

@cache_decorator
def expensive_function(arg1, arg2):
    return arg1 + arg2

result1 = expensive_function(3, 4)  
print(result1) 

result2 = expensive_function(3, 4)  
print(result2)  

result3 = expensive_function(5, 6)  
print(result3)  