# 7. Составить алгоритм решения ребуса КОТ + КОТ = ТОК (различные
# буквы означают различные цифры, старшая буква ‒ не 0).


# нет решения если кот + кот = ток
import sympy as sympy

print('вариант кот + кот = ток')
solution_1 = False
for k in range(1, 10):
    for o in range(0, 10):
        for t in range(1, 10):
            if (100*k+10*o+t)+(100*k+10*o+t) == (100*t+10*o+k):
                print('решение')
                print('kot + kot = tok')
                print(f'{k}{o}{t}+{k}{o}{t}={t}{o}{k}')
                solution_1 = True
                break
            else:
                solution_1 = False
if not solution_1:
    print('РЕШЕНИЯ НЕТ')
print('****************************************************')


# есть решение если кто + кот = ток

print('вариант кто + кот = ток')
solution_2 = False
for k in range(1, 10):
    for o in range(0, 10):
        for t in range(1, 10):
            if (100*k+10*t+o)+(100*k+10*o+t) == (100*t+10*o+k):
                print('решение')
                print('kto + kot = tok')
                print(f'{k}{t}{o}+{k}{o}{t}={t}{o}{k}')
                solution_2 = True
                break
            else:
                solution_2 = False
if solution_2:
    print('РЕШЕНИЯ НЕТ')






