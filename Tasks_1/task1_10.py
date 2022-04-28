# Число делится на 3 тогда, когда сумма его цифр делится на 3.
# Проверить этот признак на примере заданного трехзначного числа.

import numpy as np

num = np.random.randint(100, 999)
print(f'random num is {num}')
orig_num = num
sum_elements = 0
condition = False
while num != 0:
    sum_elements += num % 10
    num //= 10
sum_el_div_3 = sum_elements % 3
num_div_3 = orig_num % 3
if sum_el_div_3 == 0 and num_div_3 == 0:
    condition = True
print(f'sum_elements = {sum_elements}')
print(f'sum_el_div = {sum_el_div_3}')
print(f'num_div_3 = {num_div_3}')
if sum_el_div_3 == num_div_3 and condition:
    print('true')
else:
    print('false')

