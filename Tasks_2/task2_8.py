# 8. Натуральное число, записанное в десятичной системе счисления,
# называется сверхпростым, если оно остается простым при любой
# перестановке своих цифр. Определить все сверхпростые числа до n.

from sympy import *

# сверхпростое еще если его порядковый номер (где у 2 порядковый номер == 1)
# тоже является простым

n = int(input('введите размер списка (до n):'))
numlist = [i for i in range(1, n)]
numlist_prime = []
print(numlist)


def isNumPrime(n):
    if n == 2 or n == 3:
        return n
    if n % 2 == 0 or n < 2:
        return -1
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return -1
    else:
        return n


for i in range(1, len(numlist)):
    if isNumPrime(numlist[i]) > 0:
        numlist_prime.append(numlist[i])

print(numlist_prime)

# для проверки на простоту

isprime(101)
