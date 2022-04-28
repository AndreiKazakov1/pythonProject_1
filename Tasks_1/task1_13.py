# Для натурального числа К напечатать фразу «мы нашли К грибов в лесу»,
# согласовав окончание слова «гриб» с числом К.

import numpy as np

num = np.random.randint(10, 120)
orig_num = num
arr = []
while num != 0:
    x = num % 10
    arr.append(x)
    num //= 10
if arr[1] == 1:
    print(f'мы нашли {orig_num} грибов в лесу')
else:
    dict_mushroom = {1: 'гриб', 2: 'гриба', 3: 'гриба', 4: 'гриба',
                 0: 'грибов', 5: 'грибов', 6: 'грибов', 7: 'грибов',
                 8: 'грибов', 9: 'грибов', }
    print(f'мы нашли {orig_num} {dict_mushroom.get(arr[0])} в лесу')
