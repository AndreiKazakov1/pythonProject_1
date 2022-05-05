# 1. Шестизначный автобусный билет считается удачным, если сумма
# его цифр делится на 7. Могут ли два билета подряд быть удачными?

# билеты идут подряд

ticket_list = [i for i in range(100000, 999999)]
# print(*ticket_list)
list_of_sumOfelem = []
for i in range(len(ticket_list)):
    sumOfelem = 0
    while ticket_list[i] != 0:
        sumOfelem += ticket_list[i] % 10
        ticket_list[i] //= 10
    list_of_sumOfelem.append(sumOfelem)
# print(list_of_sumOfelem)

for i in range(len(list_of_sumOfelem)):
    if list_of_sumOfelem[i] % 7 == 0 and list_of_sumOfelem[ i +1] % 7 == 0:
        print('yes, it can be')
        break

