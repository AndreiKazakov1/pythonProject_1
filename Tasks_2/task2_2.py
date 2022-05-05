# 2. Торговая фирма в первый день работы реализовала
# товаров на P тыс. руб., а затем ежедневно увеличивала
# выручку на 3%. Какой будет выручка фирмы в тот день,
# когда она впервые превысит заданное значение Q? Сколько
# дней придется торговать фирме для достижения этого результата?

amount_of_goods = int(input('введите сумму реализации товаро в первый день : '))
stop_limit_amount = int(input('введите пороговое значение выручки : '))
incremental_turnover = amount_of_goods
count_of_days = 1
while incremental_turnover <= stop_limit_amount:
    incremental_turnover *= 1.03
    count_of_days += 1
    #print(incremental_turnover)
print(f'выручка фирмы в тот день, когда она впервые превысит заданное значение  {incremental_turnover}')
print(f' придется торговать {count_of_days} дней')

