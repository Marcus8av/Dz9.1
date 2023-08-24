# Напишите следующие функции:
# - Нахождение корней квадратного уравнения
# - Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# - Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# - Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json
from functools import wraps
from random import randint
from math import sqrt


def find_roots(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        root1 = (-b + sqrt(d)) / (2*a)
        root2 = (-b - sqrt(d)) / (2*a)
        return root1, root2
    elif d == 0:
        root = -b / (2*a)
        return root
    else:
        return "Корни в комплексных числах"


def generate_csv(filename, rows):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for _ in range(rows):
            writer.writerow([randint(1, 100) for _ in range(3)])


def use_csv(filename):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(filename, "r") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    result = func(*row, *args, **kwargs)
                    print(f"Input: {row}, Result: {result}")
        return wrapper
    return decorator

def save_to_json(filename):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {"args": args, "kwargs": kwargs, "result": result}
            with open(filename, "w") as jsonfile:
                json.dump(data, jsonfile)
        return wrapper
    return decorator

@use_csv("numbers.csv")
def find_roots_csv(a, b, c):
    return find_roots(int(a), int(b), int(c))

@save_to_json("result.json")
def find_roots_json(a, b, c):
    return find_roots(int(a), int(b), int(c))

generate_csv("numbers.csv", 100)
find_roots_csv()
find_roots_json(2, 3, 1)