# Есть натуральное двузначное число n.
# Верно ли, что среди его цифр есть 1 или 9?

import numpy as np

natNum = np.random.randint(10, 99)
print(f'натуральное двузначное число n = {natNum}')
arr = []
flg = True
while natNum != 0:
    x = natNum % 10
    arr.append(x)
    natNum //= 10
for i in range(len(arr)):
    if arr[i] == 1 or arr[i] == 9:
        flg = False
if not flg:
    print('среди  цифр этого числа есть 1 или 9')
else:
    print('среди  цифр этого числа НЕТ 1 или 9')
