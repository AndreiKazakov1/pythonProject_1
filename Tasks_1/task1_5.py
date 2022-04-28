# Определить, есть ли среди заданных целых чисел A, B, C, D
# хотя бы одно нечётное.

import numpy as np

condition = False
nums = np.random.randint(0, 100, 4)
odd_nums = []
print(nums)
for i in range(4):
    if nums[i] % 2 != 0:
        odd_nums.append(nums[i])
        condition = True
if condition:
    print("среди заданных целых чисел есть хотя бы одно нечётное")
    print(f"это значение(я) :{odd_nums}")
