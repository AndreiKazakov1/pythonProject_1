# По введенному числу (от 0 до 7) напечатать название цифры.

n = int(input('ввеите цифру от 0 до 7 :'))
n_dict = {0: 'ноль', 1: 'один', 2: 'два',
          3: 'три', 4: 'четыре', 5: 'пять',
          6: 'шесть', 7: 'семь'}
print(f'вы ввели цифру  {n_dict.get(n)}')

