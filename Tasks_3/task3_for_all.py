# Сформировать одномерный список целых чисел A, используя генератор
# случайных чисел (диапазон от 0 до 99). Размер списка n ввести с клавиатуры.
# В соответствии со своим вариантом написать программу по условию,
# представленному в таблице ниже.

import random

n = int(input("введите размер списка чисел :"))
numlist = [random.randint(0, 99) for _ in range(n)]
print(f'исходный список  {numlist}')
