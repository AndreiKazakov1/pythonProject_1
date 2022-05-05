# 1. Шестизначный автобусный билет считается удачным, если сумма
# его цифр делится на 7. Могут ли два билета подряд быть удачными?

import random

ticket_list = [random.randint(100000, 999999) for _ in range(20)]
print(*ticket_list)
list_of_sumOfelem = []
for i in range(len(ticket_list)):
    sumOfelem = 0
    while ticket_list[i] != 0:
        sumOfelem += ticket_list[i] % 10
        ticket_list[i] //= 10
    list_of_sumOfelem.append(sumOfelem)
print(list_of_sumOfelem)
try:
    for i in range(len(list_of_sumOfelem)):
        if list_of_sumOfelem[i] % 7 == 0 and list_of_sumOfelem[i+1] % 7 == 0:
            print('yes, it can be')
            break
except Exception:
    print('the next element in list is not exists')
